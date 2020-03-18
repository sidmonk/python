def prm(M):
    print('\n'.join([' '.join([str(j).ljust(5) for j in i]) for i in M]))
    print()

M = [[True, False, True], [False, False, True], [True, True, False]]
n = len(M)
W = [[j for j in i] for i in M]

for k in range(n):
    for i in range(n):
        for j in range(n):
            W[i][j] = W[i][j] or (W[i][k] and W[k][j])

prm(M)
prm(W)