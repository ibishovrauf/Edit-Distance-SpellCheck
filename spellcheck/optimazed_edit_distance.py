# optimazed_edit_distance.py


def optimazed_edit_distance(word1:str, word2:str):
    """
    Calculates the minimum edit distance between two words using an optimized dynamic programming approach.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        int: The minimum edit distance between the two words.
    """

    m = len(word1)
    n = len(word2)
    
    # Create a matrix to store the intermediate distances
    dp = [[0] * (n + 1) for _ in range(2)]
    
    # Initialize the first row and column of the matrix
    for j in range(n + 1):
        dp[0][j] = j
    # Calculate the minimum distance
    for i in range(1, m + 1):
        dp[i % 2][0] = i
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
            else:
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[i % 2][j - 1], dp[(i - 1) % 2][j]) + 1
    
    return dp[m % 2][n]


def main():
    """
    Entry point for command-line usage.
    """
    import sys

    if len(sys.argv) != 3:
        print("Usage: python optimazed_edit_distance.py <string1> <string2>")
        sys.exit(1)

    str1 = sys.argv[1]
    str2 = sys.argv[2]

    distance = optimazed_edit_distance(str1, str2)
    print(f"Edit distance between '{str1}' and '{str2}': {distance}")


if __name__ == "__main__":
    main()
