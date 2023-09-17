# edit_distance.py

def edit_distance(str1: str, str2: str):
    """
    Calculates the minimum edit distance between two strings using a recursive approach.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The minimum edit distance between the two strings.
    """
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Check if last characters are the same
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    
    # If last characters are different, consider all three operations
    insert = edit_distance(str1, str2[:-1]) + 1  # Insertion
    delete = edit_distance(str1[:-1], str2) + 1  # Deletion
    substitute = edit_distance(str1[:-1], str2[:-1]) + 1  # Substitution
    
    return min(insert, delete, substitute)

def main():
    """
    Entry point for command-line usage.
    """
    import sys

    if len(sys.argv) != 3:
        print("Usage: python edit_distance.py <string1> <string2>")
        sys.exit(1)

    str1 = sys.argv[1]
    str2 = sys.argv[2]

    distance = edit_distance(str1, str2)
    print(f"Edit distance between '{str1}' and '{str2}': {distance}")


if __name__ == "__main__":
    main()
