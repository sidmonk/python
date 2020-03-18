import random

A = [random.randint(0, 50) for i in range(15)]
A.sort()
print(A)


def binfind(A, a):
    if A == []:
        return None
    l = 0
    r = len(A) - 1
    m = (l + r) // 2
    guess = A[m]
    if guess == a:
        return m
    elif a > guess:
        l = m + 1
        rec = binfind(A[l: r + 1], a)
        if rec != None:
            return l + rec
    else:
        r = m - 1
        return binfind(A[l: r + 1 ], a)
    return None

rand = random.randint(0, 50)
print(rand)
print(binfind(A, rand))