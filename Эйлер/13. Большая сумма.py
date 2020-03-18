f = open('13.txt', 'r')
A = []
A = [[int(i) for i in line.strip()]for line in f]
f.close()

M = len(A)
N = len(A[0])
S = [0]*(N + 2)
for j in range(N - 1, -1, -1):
    s = 0
    for i in range(M):
        s += A[i][j]
    s1 = str(s)[::-1]
    for i in range(len(s1)):
        S[i + (N - 1 - j)] += int(s1[i])
    for i in range(len(S)):
        if S[i] >= 10:
            S[i + 1] += S[i] // 10
            S[i] %= 10

ans = ''
for i in range(len(S) - 1, -1, -1):
    ans += str(S[i])
print(ans)