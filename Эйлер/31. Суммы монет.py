def razm(A, s):
    A = [i for i in A]
    if s == 0 or len(A) == 1:
        return 1
    elif A[-1] > s:
        return razm(A[: -1], s)
    else:
        return razm(A[: -1], s) + razm(A, s - A[-1])

print(razm([1, 2, 5, 10, 20, 50, 100, 200], 200))


