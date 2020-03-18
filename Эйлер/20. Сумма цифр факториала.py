"""n! означает n × (n − 1) × ... × 3 × 2 × 1
Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Найдите сумму цифр в числе 100!"""


from math import factorial


summ = 0
s = factorial(100)
for i in str(s):
    summ += int(i)

print(summ)