# spellcheck.py
from . import optimazed_edit_distance, weighted_edit_distance, edit_distance

def spell_checker(word:str, dictionary: list, optimazed = False, weighted = False):
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
            distance = weighted_edit_distance(word, dict_word, insertion_cost=1, deletion_cost=2, substitution_cost=3)
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
