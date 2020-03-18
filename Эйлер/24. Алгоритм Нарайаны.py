'''Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?'''

from math import factorial
A = [i for i in range(10)]
n = factorial(len(A))
B = []
Comb = []
s = ''
for i in A:
    s += str(i)
Comb += [int(s)]
s = ''

for k in range(n - 1):
    for i in range(len(A) - 1, 0, -1):
        if A[i - 1] < A [i]:
            p = i - 1
            break
    for j in A[p + 1: ]:
        if j > A[p]:
            B.append(j)
    min_suf = A.index(min(B))
    B.clear()
    A[p], A[min_suf] = A[min_suf], A[p]
    A[p + 1:] = sorted(A[p + 1:])
    for i in A:
        s += str(i)
    Comb += [int(s)]
    s = ''

print(Comb[1000000])