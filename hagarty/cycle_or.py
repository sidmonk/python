M = [[False, True, False, False, False],
     [False, False, True, False, False],
     [False, False, False, False, True],
     [False, False, True, False, False],
     [False, False, False, True, False]]


def cycles(M):
    n = len(M)
    colors = ['white' for i in range(n)]
    having_cycle = False

    def cdfs(i):
        nonlocal having_cycle
        colors[i] = 'gray'
        for j in range(n):
            if M[i][j]:
                if colors[j] == 'gray':
                    having_cycle = True
                    break
                elif colors[j] == 'white':
                    cdfs(j)
        colors[i] = 'black'

    for i in range(n):
        if having_cycle:
            return having_cycle
        if colors[i] == 'white':
            cdfs(i)
    return False

print(cycles(M))