# weighted_edit_distance.py

def weighted_edit_distance(str1:str, str2:str, insertion_cost:int=1, deletion_cost:int=1, substitution_cost:int=1):
    """
    Calculates the minimum edit distance between two strings with weighted costs for each operation.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.
        insertion_cost (int): The cost of an insertion operation (default: 1).
        deletion_cost (int): The cost of a deletion operation (default: 1).
        substitution_cost (int): The cost of a substitution operation (default: 1).

    Returns:
        int: The minimum edit distance between the two strings.
    """

    m = len(str1)
    n = len(str2)
    
    # Create a matrix to store the intermediate distances
    dp = [[0] * (n + 1) for _ in range(2)]
    
    # Initialize the first row and column of the matrix
    for j in range(n + 1):
        dp[0][j] = j
    # Calculate the minimum distance
    for i in range(1, m + 1):
        dp[i % 2][0] = i
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
            else:
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1]+substitution_cost, dp[i % 2][j - 1]+insertion_cost, dp[(i - 1) % 2][j]+deletion_cost)
    
    return dp[m % 2][n]
def main():
    """
    Entry point for command-line usage.
    """
    import sys

    if len(sys.argv) != 3:
        print("Usage: python weighted_edit_distance.py <string1> <string2>")
        sys.exit(1)

    str1 = sys.argv[1]
    str2 = sys.argv[2]

    distance = weighted_edit_distance(str1, str2)
    print(f"Edit distance between '{str1}' and '{str2}': {distance}")


if __name__ == "__main__":
    main()
