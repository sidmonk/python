from datetime import *
from math import sqrt

start_time = datetime.now()
n = 10**5

flag = [False for i in range(n+1)]

for i in range(int(sqrt(n))+1):
    for j in range(int(sqrt(n))+1):
        a = 4*i**2 + j**2
        if a <= n and (a % 12 == 1 or a % 12 == 5):
            flag[a] = not flag[a]
        a -= i**2
        if a <= n and (a % 12 == 7):
            flag[a] = not flag[a]
        a -= 2*j**2
        if i > j and a <= n and a % 12 == 11:
            flag[a] = not flag[a]

for i in range(5, int(sqrt(n))+1):
    if flag[i]:
        p = i**2
        k = p
        while k <= n:
            flag[k] = False
            k += p

flag[1] = False
flag[2] = True
flag[3] = True
end_time = datetime.now()

simp = set()
for i in range(n+1):
    if flag[i]:
        simp.add(i)


print(len(simp))
print(f'Duration: {end_time - start_time}')