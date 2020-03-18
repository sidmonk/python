from datetime import *
from math import sqrt

start_time = datetime.now()
n = 10**2

def Erat(n):
    A = {2} | set(i for i in range(3, n + 1, 2))
    for p in range(3, int(sqrt(n) + 1), 2):
        d_e = p**2
        while d_e < n:
            A.discard(d_e)
            d_e += 2*p
    return A

if __name__ == '__main__':
    A = Erat(n)
    print(len(A))
    end_time = datetime.now()
    print(f'Duration: {end_time - start_time}')



def simplen(n):
    if n == 2:
        return True
    elif n == 0 or n == 1 or n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

# for i in A:
#     if not simplen(i):
#         print('алгоритм - говно')




