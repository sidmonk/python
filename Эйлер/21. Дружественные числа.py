"""
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b -
дружественным числом. Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110,
поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
Подсчитайте сумму всех дружественных чисел меньше 10000.
"""


from sito import *


def sum_del(n):
    ans = 1
    for i in range(2, n):
        if n % i == 0:
            ans += i
    return ans

n = 284

sum_drug = 0

for i in range(10000):
    sd = sum_del(i)
    if sd == 1:
        continue
    if sum_del(sd) == i and sd != i and sd < 10000:
        print(i, sd)
        sum_drug += i


print(sum_del(sum_drug))