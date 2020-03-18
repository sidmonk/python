n = 11
A = [[i*j for j in range(n)] for i in range(n)]

for i in range(1, n):
    print(' '.join([str(A[i][j]).ljust(3) for j in range(1, n)]))