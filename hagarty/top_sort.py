M = [[False, False, False, False, False, False, False, False],
     [True, False, False, False, False, False, False, False],
     [False, True, False, True, False, False, True, False],
     [False, False, False, False, True, False, False, False],
     [False, False, False, False, False, True, False, False],
     [False, False, False, False, False, False, False, False],
     [False, False, False, False, True, False, False, False],
     [False, False, True, False, False, False, False, False]]




def top_sort(M):
    n = len(M)
    colors = ['white' for i in range(n)]
    leave = []
    having_cycle = False

    def dfs(i):
        nonlocal having_cycle
        colors[i] = 'gray'
        for j in range(n):
            if M[i][j]:
                if colors[j] == 'gray':
                    having_cycle = True
                    break
                elif colors[j] == 'white':
                    dfs(j)
        colors[i] = 'black'
        if i not in leave:
            leave.append(i)

    for i in range(n):
        dfs(i)
        if having_cycle:
            return 'Having cycle'

    leave.reverse()
    return leave

print(top_sort(M))
