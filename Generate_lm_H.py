#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:38:17 2020

@author: HS45858
"""

#import argparse
import gzip
import io
import os
import subprocess
from collections import Counter

import progressbar


def convert_and_filter_topk(input_loc, output_loc, top_k):
    """ Convert to lowercase, count word occurrences and save top-k words to a file """

    counter = Counter()
    data_lower = os.path.join(output_loc, "lower.txt.gz")

    print("\nConverting to lowercase and counting word occurrences ...")
    with io.TextIOWrapper(
        io.BufferedWriter(gzip.open(data_lower, "w+")), encoding="utf-8"
    ) as file_out:

        # Open the input file either from input.txt or input.txt.gz
        _, file_extension = os.path.splitext(input_loc)
        if file_extension == ".gz":
            file_in = io.TextIOWrapper(
                io.BufferedReader(gzip.open(input_loc)), encoding="utf-8"
            )
        else:
            file_in = open(input_loc, encoding="utf-8")

        for line in progressbar.progressbar(file_in):
            line_lower = line.lower()
            counter.update(line_lower.split())
            file_out.write(line_lower)

        file_in.close()

    # Save top-k words
    print("\nSaving top {} words ...".format(top_k))
    top_counter = counter.most_common(top_k)
    vocab_str = "\n".join(word for word, count in top_counter)
    vocab_path = "vocab-{}.txt".format(top_k)
    vocab_path = os.path.join(output_loc, vocab_path)
    with open(vocab_path, "w+") as file:
        file.write(vocab_str)

    print("\nCalculating word statistics ...")
    total_words = sum(counter.values())
    print("  Your text file has {} words in total".format(total_words))
    print("  It has {} unique words".format(len(counter)))
    top_words_sum = sum(count for word, count in top_counter)
    word_fraction = (top_words_sum / total_words) * 100
    print(
        "  Your top-{} words are {:.4f} percent of all words".format(
            top_k, word_fraction
        )
    )
    print('  Your most common word "{}" occurred {} times'.format(*top_counter[0]))
    last_word, last_count = top_counter[-1]
    print(
        '  The least common word in your top-k is "{}" with {} times'.format(
            last_word, last_count
        )
    )
    for i, (w, c) in enumerate(reversed(top_counter)):
        if c > last_count:
            print(
                '  The first word with {} occurrences is "{}" at place {}'.format(
                    c, w, len(top_counter) - 1 - i
                )
            )
            break

    return data_lower, vocab_str


def build_lm(output_loc, kenlm_bins, arpa_order, max_arpa_memory, arpa_prune, binary_a_bits, binary_q_bits, binary_type, data_lower, vocab_str):
    print("\nCreating ARPA file ...")
    lm_path = os.path.join(output_loc, "lm.arpa")
    subargs = [
            os.path.join(kenlm_bins, "lmplz"),
            "--order",
            str(arpa_order),
            "--temp_prefix",
            output_loc,
            "--memory",
            max_arpa_memory,
            "--text",
            data_lower,
            "--arpa",
            lm_path,
            "--prune",
            *arpa_prune.split("|"),
        ]
    
    
    subargs += ["--discount_fallback"]
    subprocess.check_call(subargs)

    # Filter LM using vocabulary of top-k words
    print("\nFiltering ARPA file using vocabulary of top-k words ...")
    filtered_path = os.path.join(output_loc, "lm_filtered.arpa")
    subprocess.run(
        [
            os.path.join(kenlm_bins, "filter"),
            "single",
            "model:{}".format(lm_path),
            filtered_path,
        ],
        input=vocab_str.encode("utf-8"),
        check=True,
    )

    # Quantize and produce trie binary.
    print("\nBuilding lm.binary ...")
    binary_path = os.path.join(output_loc, "lm.binary")
    subprocess.check_call(
        [
            os.path.join(kenlm_bins, "build_binary"),
            "-a",
            str(binary_a_bits),
            "-q",
            str(binary_q_bits),
            "-v",
            binary_type,
            filtered_path,
            binary_path,
        ]
    )


def main():
    input_loc = 'data/queries.txt'
   
    """" parser = argparse.ArgumentParser(
        description="Generate lm.binary and top-k vocab for DeepSpeech."
    )
    parser.add_argument(
        "--input_txt",
        help="Path to a file.txt or file.txt.gz with sample sentences",
        type=str,
        required=True,
    )""" 
    
    
    
    """parser.add_argument(
        "--output_dir", help="Directory path for the output", type=str, required=True
    )"""
    
    
    output_loc = '.'
    
    """parser.add_argument(
        "--top_k",
        help="Use top_k most frequent words for the vocab.txt file. These will be used to filter the ARPA file.",
        type=int,
        required=True,
    )"""
    
    top_k = 500000
    
    
    """parser.add_argument(
        "--kenlm_bins",
        help="File path to the KENLM binaries lmplz, filter and build_binary",
        type=str,
        required=True,
    )"""
    
    kenlm_bins = 'kenlm/build/bin/'
    
    
    """parser.add_argument(
        "--arpa_order",
        help="Order of k-grams in ARPA-file generation",
        type=int,
        required=True,
    )"""
    
    arpa_order = 5
    
    """parser.add_argument(
        "--max_arpa_memory",
        help="Maximum allowed memory usage for ARPA-file generation",
        type=str,
        required=True,
    )"""
    
    max_arpa_memory = "85%"
    
    
    """parser.add_argument(
        "--arpa_prune",
        help="ARPA pruning parameters. Separate values with '|'",
        type=str,
        required=True,
    )"""
    
    arpa_prune = "0|0|1"
    
    
    """parser.add_argument(
        "--binary_a_bits",
        help="Build binary quantization value a in bits",
        type=int,
        required=True,
    )"""
    
    binary_a_bits = 255
    
    """parser.add_argument(
        "--binary_q_bits",
        help="Build binary quantization value q in bits",
        type=int,
        required=True,
    )"""
    
    binary_q_bits =  8
    
    
    """parser.add_argument(
        "--binary_type",
        help="Build binary data structure type",
        type=str,
        required=True,
    )"""
    
    binary_type = 'trie'
    
    
    """parser.add_argument(
        "--discount_fallback",
        help="To try when such message is returned by kenlm: 'Could not calculate Kneser-Ney discounts [...] rerun with --discount_fallback'",
        action="store_true",
    )"""
    
    

    #args = parser.parse_args()

    data_lower, vocab_str = convert_and_filter_topk(input_loc, output_loc, top_k)
    build_lm(output_loc, kenlm_bins, arpa_order, max_arpa_memory, arpa_prune, binary_a_bits, binary_q_bits, binary_type, data_lower, vocab_str)

    # Delete intermediate files
    os.remove(os.path.join(output_loc, "lower.txt.gz"))
    os.remove(os.path.join(output_loc, "lm.arpa"))
    os.remove(os.path.join(output_loc, "lm_filtered.arpa"))
    #os
    
    """alphabet_loc = 'alphabet.txt'
    lm_loc = 'lm.binary'
    """
    
    subprocess.check_call([r"./generate_scorer_package",
            "--alphabet",
            './alphabet.txt',
            "--lm",
            './lm.binary',
            "--vocab",
            './vocab-500000.txt',
            "--package",
            './kenlm1.scorer',
            "--default_alpha",
            str(0.931289039105002),
            "--default_beta",
            str(1.1834137581510284),])
    #os.system("./generate_scrorer_package")
    
    """parameters = [
            r"./generate_scrorer_package",
            "--alphabet",
            alphabet.txt,
            "--lm",
            lm.binary,
            "--vocab",
            vocab-500000.txt,
            "--package",
            kenlm1.scorer,
            "--default_alpha",
            0.931289039105002,
            "--default_beta",
            1.1834137581510284,
        ]
    """
    
if __name__ == "__main__":
    main()
