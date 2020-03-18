import time
import collections

N = 10**3
A = [[0 for i in range(N)]for j in range(N)]

i = 0
j = 0
A[i][j]
way = N
cur_way = way
ihod, jhod = 0, 1

t1 = time.time()

for n in range(N**2):
    A[i][j] = n
    cur_way += 1
    if cur_way == way:
        ihod, jhod = -jhod, -ihod
    if cur_way == 2*way:
        ihod, jhod = jhod, ihod
        way -= 1
        cur_way = 0
    i += ihod
    j += jhod

t2 = time.time()

print(t2-t1)

# for i in A:
#     print(''.join([str(j).ljust(3) for j in i]))
