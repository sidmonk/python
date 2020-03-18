from _collections import defaultdict
from svyaz import svyaz

M = [[False, True, False, False],
     [True, False, False, True],
     [True, False, False, True],
     [False, False, True, False]]


def find_comp(M):
    n = len(M)
    if svyaz(M):
        return list(range(n))

    visited = [False for i in range(n)]
    order = []

    def dfs1(i):
        visited[i] = True
        for j in range(n):
            if M[i][j] and not visited[j]:
                dfs1(j)
        order.append(i)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    component = [0 for i in range(n)]
    col = 1

    def invert(M):
        M1 = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    M1[j][i] = True
        return M1

    M1 = invert(M)

    def dfs2(i):
        component[i] = col
        for j in range(n):
            if M1[i][j] and component[j] == 0:
                dfs2(j)

    for i in order[::-1]:
        if component[i] == 0:
            dfs2(i)
            col += 1


    ans = defaultdict(list)
    for i in range(len(component)):
        ans[component[i]].append(i)
    return list(ans.values())


print(find_comp(M))