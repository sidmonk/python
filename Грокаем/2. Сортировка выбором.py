import random
A = [random.randint(0, 50) for i in range(10)]


imin = 0
for i in range(len(A)):
    imin = min(range(i, len(A)), key=A.__getitem__)
    A[i], A[imin] = A[imin], A[i]

print(A)