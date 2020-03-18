M = [[False, True, True, False, False, False],
     [False, False, True, True, False, False],
     [False, False, False, True, False, False],
     [False, False, False, False, True, True],
     [False, True, False, False, False, False],
     [False, False, False, False, True, False]]

inf = float('inf')
w =[[0, 3, 10, inf, inf, inf],
    [inf, 0, 11, 12, inf, inf],
    [inf, inf, 0, 5, inf, inf],
    [inf, inf, inf, 0, 2, 8],
    [inf, 4, inf, inf, 0, inf],
    [inf, inf, inf, inf, 6, 0]]

def deikstra(M, w, st=0):
    n = len(M)
    not_visited = set(range(n))
    d = [w[st][j] for j in range(n)]
    ways = [str(st) + str(i) for i in range(n)]
    not_visited.discard(st)

    while not_visited:
        u = min(not_visited, key=d.__getitem__)
        not_visited.discard(u)
        for j in not_visited:
            if M[u][j]:
                d1 = d[u] + w[u][j]
                if d1 < d[j]:
                    d[j] = d1
                    ways[j] = ways[u] + str(j)
        for i in range(n):
            if d[i] == inf:
                ways[i] = 'No'
    return d, ways

print(deikstra(M, w, 2))