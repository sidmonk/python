def F(A, S):
    inf = float("inf")
    if S == 0:
        return 0
    elif len(A) == 0:
        return inf
    elif A[-1] > S:
        return F(A[:-1], S)
    else:
        return 1 + min([F(A, S - i) for i in A])



print(F([50, 100, 500, 1000, 5000], 18750))