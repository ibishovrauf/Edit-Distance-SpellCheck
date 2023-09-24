# spellcheck.py
import sys
import os
import argparse

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root directory to the Python path
sys.path.insert(0, project_root)

import json
from spellcheck import optimazed_edit_distance, weighted_edit_distance, edit_distance

def spell_checker(word:str, dictionary: list, optimazed = False, weighted = False, weights = [1, 2, 3]):
    """
    Corrects a word based on the minimum edit distance from a dictionary of valid words.

    Args:
        word (str): The word to be corrected.
        dictionary (list): A list of valid words.
        optimazed (bool): indicate whether to use optimazed edit distance or not 
        weighted (bool):  indicate whether to use weighted edit distance or not

    Returns:
        dict: A dictionary containing the following information:
            - 'probability' (float): The probability (0 in this case).
            - 'from' (str): The input 'word'.
            - 'to' (str): An empty string.
            - 'cost' (int): The minimum distance from 'word' to the 'word'.
    """

    min_distance = float('inf')
    corrected_word = {"probability": 0, "from":word, "to":"", "cost": min_distance}
    
    for dict_word in dictionary:
        if weighted:
            distance = weighted_edit_distance(word, dict_word, insertion_cost=weights[0], deletion_cost=weights[1], substitution_cost=weights[2])
        elif optimazed:
            distance = optimazed_edit_distance(word, dict_word)
        else:
            distance = edit_distance(word, dict_word)
        if distance < min_distance:
            min_distance = distance
            corrected_word["to"] = dict_word
            corrected_word["cost"] = distance
            corrected_word["probability"] = 1/(distance+1)
    
    return corrected_word

def main():
    """
    Entry point for command-line usage.
    """
    parser = argparse.ArgumentParser(description="SpellCheck tool")

    algoritm = [0, 0, 0]
    parser.add_argument("--input", help="Input word to spellcheck")
    parser.add_argument(
        "--algorithm",
        choices=["optimized", "weighted", "normal"],
        default="optimized",
        help="Specify the spellcheck algorithm to use (default: optimized)",
    )

    parser.add_argument(
        "--weights",
        nargs="+",
        type=float,
        help="Custom weights for the weighted algorithm (space-separated values)",
    )


    args = parser.parse_args()

    algoritm[["optimized", "weighted", "normal"].index(args.algorithm)] = 1

    with open('data/test_data.json', 'r') as file:
        calc_data = json.load(file)

    result = spell_checker(args.input, calc_data, optimazed=algoritm[0], weighted=algoritm[1])

    print(f"\nCorrected form of word '{args.input}': {result['to']} with probability: {result['probability']}\n")


if __name__ == "__main__":
    main()
