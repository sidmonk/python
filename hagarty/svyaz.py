M = [[False, True, False, False, False],
     [False, False, True, False, False],
     [False, False, False, False, True],
     [False, False, True, False, False],
     [False, False, False, False, False]]

def svyaz(M):
    n = len(M)
    visited = [False for i in range(n)]

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if M[i][j] and not visited[j]:
                dfs(j)

    dfs(0)
    return all(visited)

if __name__ == '__main__':
    print(svyaz(M))