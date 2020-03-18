import numpy as np

with open('11') as f:
    A = np.array([[int(j) for j in i.split()] for i in f])

def maxfour(A, n=4):
    ans = 0
    for i in A:
        for j in range(len(i) - n + 1):
            four = 1
            for k in range(n):
                four *= i[j+k]
            ans = max(ans, four)
    return ans

def glav_diag(A, n=4):
    return [A.diagonal(i) for i in range(n - len(A), len(A) - n + 1)]


print(max([maxfour(i) for i in (A, A.transpose(), glav_diag(A), glav_diag(A[:,::-1]))]))