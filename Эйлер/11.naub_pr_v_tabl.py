
A = []
with open('11') as f:
    for i in f:
        A.append([int(i) for i in i.split()])

n = len(A[0])
maxpr = 1
nmax = 4


def max_four(A, n=nmax):
    max = 0
    if len(A) < n:
        return
    for i in range(len(A) - n + 1):
        sr = A[i: i + n]
        if 0 in sr:
            continue
        else:
            pr = 1
            for j in sr:
                pr *= j
            if pr > max:
                max = pr
    return max

for i in range(n):
    v = []
    for j in range(n):
        v.append(A[i][j])
    maxpr = max(maxpr, max_four(v))

for j in range(n):
    v = []
    for i in range(n):
        v.append(A[i][j])
    maxpr = max(maxpr, max_four(v))

for k in range(n):
    v = []
    for j in range(n - k):
        v.append(A[k+j][j])
    if len(v) < nmax:
        break
    maxpr = max(maxpr, max_four(v))

for k in range(1, n):
    v = []
    for j in range(k, n):
        v.append(A[k-j][j])
    if len(v) < nmax:
        break
    maxpr = max(maxpr, max_four(v))

for k in range(n-1, 0, -1):
    v = []
    for j in range(k+1):
        v.append(A[k-j][j])
    if len(v) < nmax:
        break
    maxpr = max(maxpr, max_four(v))

for k in range(n, 2*(n-1) + 1):
    v = []
    for j in range(k-n+1, n):
        v.append(A[k-j][j])
    if len(v) < nmax:
        break
    maxpr = max(maxpr, max_four(v))
print(maxpr)


