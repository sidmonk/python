from _datetime import *
from SITO import Erat


n = 1000

def mnoj(n):
    A = sorted(Erat(n))
    mn = dict()
    ans = f'{n} = '

    for i in A:
        while n % i == 0:
            mn[i] = mn.get(i, 0) + 1
            n /= i
    ans += '*'.join([f'{key}^{value}' for key, value in mn.items()])
    return ans

print(mnoj(n))


