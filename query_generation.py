import os
import shutil
# from tqdm.notebook import tqdm
from tqdm import tqdm
import pandas as pd
import numpy as np
import re
from itertools import combinations, combinations_with_replacement
max_words = 3
loc_vocab = "data/vocab-tagged.xlsx"
loc_queries = "data/queries.txt"

vocab = pd.read_excel(loc_vocab)

vocab = {k: [val for val in v if pd.notnull(val)] for k, v in vocab.to_dict(orient="list").items()}
vocab["collateral"].extend(vocab.pop("legal_entity"))


def generate_queries(initial_operators, join_operators, intersection_operators, collateral, clause_operators=None,
                     max_words=max_words, write_to_file="queries.txt", cleanup=True, verbose=True):
    queries = []
    if write_to_file:
        created_dirs = []
        created_files = []
        tmp_dir = "queries_tmp"
        os.makedirs(tmp_dir, exist_ok=False)
        created_dirs.append(tmp_dir)
    for initial_operator in initial_operators + intersection_operators:
        if write_to_file:
            queries = []
        query = initial_operator
        assets_combinations = []
        join_operators_combinations = []
        if max_words is None:
            max_words = len(collateral)
        for r in range(1, max_words):
            assets_combinations.extend(list(combinations(collateral, r)))
            list_len = r - 1
            if list_len:
                join_operators_combinations.extend([['and'] * i + ['but not'] + ['and'] * (list_len-i - 1) for i in range(list_len)])
            else:
                join_operators_combinations.extend([[op] for op in join_operators])
        assets_generator = tqdm(assets_combinations, desc="Generating initial queries") if verbose else assets_combinations
        for assets_combination in assets_generator:
            if len(assets_combination) == 1:
                body = ""
                body += f"{assets_combination[0]} "
                queries.append(f"{query} {body}".strip())
            else:
                for join_operator_combination in [j for j in join_operators_combinations if
                                                  len(j) == (len(assets_combination) - 1)]:
                    body = ""
                    query_len = len(assets_combination)
                    for a in range(query_len):
                        body += f"{assets_combination[a]} "
                        if a < (query_len - 1):
                            body += f"{join_operator_combination[a]} "
                    queries.append(f"{query} {body}".strip())
        if write_to_file:
            filename = f"{tmp_dir}/{initial_operator}.txt"
            with open(filename, "a") as f:
                f.write("\n")
                f.write("\n".join(queries))
            created_files.append(filename)

    if write_to_file:
        intersection_generator = tqdm(intersection_operators, desc=f"Joining {intersection_operators[0]}") if verbose else intersection_operators
        for intersection_operator in intersection_generator:
            intersection_file_path = f"{tmp_dir}/{intersection_operator}.txt"
            intersection_query = None
            # open file with queries starting with one of the intersection operators to iterate over queries
            with open(intersection_file_path, "r") as intersection_file:
                intersection_query = intersection_file.readline()
                while intersection_query != "":
                    if intersection_query.strip() != "":  # check whether the read line is not a blank line
                        initial_generator = initial_operators
                        for initial_operator in initial_generator:
                            initial_file_path = f"{tmp_dir}/{initial_operator}.txt"
                            initial_query = None
                            # open file with queries starting with one of the initial operators to iterate over queries
                            with open(initial_file_path, "r") as initial_file:
                                initial_query = initial_file.readline()
                                while initial_query != "":  # check whether the read line is not a blank line
                                    if initial_query.strip() != "":
                                        joined_query = f"{initial_query.strip()} and {intersection_query.strip()}\n"
                                        with open(write_to_file, "a") as all_queries_file:
                                            all_queries_file.write(f"{initial_query.strip()}\n")
                                            all_queries_file.write(joined_query)
                                    initial_query = initial_file.readline()
                    intersection_query = intersection_file.readline()
#             print(f"Completed {intersection_operator}.")
        if cleanup:
            for file in created_files:
                os.remove(file)
            for dir in created_dirs:
                shutil.rmtree(dir)
        return write_to_file
    else:
        all_queries = []
        for initial_operator in initial_operators:
            for intersection_operator in intersection_operators:
                intersection_queries = [query for query in queries if re.search(fr"^(?!{intersection_operator})", query)]
                initial_queries = [query for query in queries if re.search(fr"^(?!{initial_operator})", query)]
                joined_queries = [f"{initial_query} and {intersection_query}" for initial_query in initial_queries for intersection_query in intersection_queries]
                all_queries.append(joined_queries)
            all_queries.extend(initial_queries)
    
        return all_queries


queries = generate_queries(**vocab)
