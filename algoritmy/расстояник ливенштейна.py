def livenshtein(s1:str, s2:str):
    """
    >>> livenshtein('корова', 'молоко')
    4
    """
    # чтобы не заполнять нулевые строки отдельно. livens[0][j] = j; livens[i][0] = i
    livens = [[i+j if i*j == 0 else 0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                livens[i][j] = livens[i-1][j-1]
            else:
                livens[i][j] = 1 + min(livens[i-1][j-1], livens[i][j-1], livens[i-1][j])
    return livens[-1][-1]


if __name__ == '__main__':
    import doctest
    # тесты в документации
    doctest.testmod()   # verbose=True покажет все результаты тестов, а не только фэйлы