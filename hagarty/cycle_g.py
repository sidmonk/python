M = [[False, True, False, False, False],
     [True, False, True, False, False],
     [False, True, False, True, False],
     [False, False, True, False, True],
     [False, True, False, True, False]]

def cycle(M):
    n = len(M)
    colors = ['white' for i in range(n)]
    having_cycle = False

    def cdfs(i, lust=None):
        nonlocal having_cycle
        colors[i] = 'gray'
        for j in range(n):
            if M[i][j] and j != lust:
                if colors[j] == 'gray':
                    having_cycle = True
                    break
                elif colors[j] == 'white':
                    cdfs(j, i)
        colors[i] = 'black'

    for i in range(n):
        cdfs(i)
        if having_cycle:
            return having_cycle
    return False

print(cycle(M))