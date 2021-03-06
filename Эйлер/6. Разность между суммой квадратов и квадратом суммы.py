'''
Сумма квадратов первых десяти натуральных чисел равна 1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел равен (1 + 2 + ... + 10)^2 = 55^2 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет
3025 − 385 = 2640. Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
'''


import time

t1 = time.time()
n = 10**7


t1 = time.time()
ssq = sum([i**2 for i in range(1, n + 1)])
sqs = sum([i for i in range(1, n + 1)])**2
t2 = time.time()
print(t2 - t1)
