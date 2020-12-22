import pandas as pd
import numpy as np
import re
from itertools import combinations, combinations_with_replacement

loc_vocab = "data/vocab-tagged.xlsx"
loc_queries = "data/queries.txt"

vocab = pd.read_excel(loc_vocab)

vocab = {k: [val for val in v if pd.notnull(val)] for k, v in vocab.to_dict(orient="list").items()}
vocab["collateral"].extend(vocab.pop("legal_entity"))


def generate_queries(initial_operators, join_operators, collateral, clause_operators=None):
    queries = []
    for initial_operator in initial_operators:
        query = initial_operator
        assets_combinations = []
        join_operators_combinations = []
        for r in range(1, len(collateral)):
            assets_combinations.extend(list(combinations(collateral, r)))
            join_operators_combinations.extend(list(combinations_with_replacement(join_operators, r)))
        for assets_combination in assets_combinations:
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
    not_has_posted_queries = [query for query in queries if re.search(r"^(?!has posted)", query)]
    has_posted_queries = [query for query in queries if re.search(r"^(has posted)", query)]
    joined_queries = []
    for not_has_posted_query in not_has_posted_queries:
        for has_posted_query in has_posted_queries:
            joined_queries.append(not_has_posted_query + " and " + has_posted_query)

    not_has_posted_queries.extend(joined_queries)

    return not_has_posted_queries


queries = generate_queries(**vocab)
with open(loc_queries, "w") as f:
    for query in queries:
        f.write(query + "\n")
    f.close()
