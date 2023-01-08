def levenshtein_distance(i, j, s1, s2, matrix):
    """ Calculate Levenshtein distance for 1 line

    Args:
        i (int): matrix line number
        j (int): matrix column number
        s1 (file): first file
        s2 (file): second file
        matrix (array n*m): matrix

    Returns:
        int: minimal value
    """
    if i == 0 and j == 0:
        return 0
    elif j == 0 and i > 0:
        return i
    elif i == 0 and j > 0:
        return j
    else:
        m = 0 if s1[i-1] == s2[j-1] else 1
        return min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+m)

def calculate_levenshtein_distance(s1, s2):
    """ Calculate Levenshtein distance for 2 files

    Args:
        s1 (file): _description_
        s2 (file): _description_

    Returns:
        int: matrix[n][m]
    """
    n = len(s1)
    m = len(s2)
    matrix = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            matrix[i][j] = levenshtein_distance(i, j, s1, s2, matrix)
    return matrix[n][m]

with open('input.txt', encoding='utf-8') as file:
    s = file.readlines()
    for i in range(len(s)):
        Line = s[i]
        probel = Line.find(' ')
        with open(Line[:probel], encoding='utf-8') as file_1:
            s_1 = file_1.read()
        with open(Line[probel + 1:len(Line[i]) - 2], encoding='utf-8') as file_2:
            s_2 = file_2.read()
        result = 1 - calculate_levenshtein_distance(s_1, s_2) / len(s_2)
        with open('scores.txt', 'a', encoding='utf-8') as scores:
            scores.write(str(result))
            scores.write('\n')