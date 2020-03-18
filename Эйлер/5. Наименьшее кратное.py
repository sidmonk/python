'''
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''

from sito import *

n = 20
k = 1

ans = NOK(*tuple([i for i in range(2, n + 1)]))
itog = 1
for key, value in ans.items():
    itog *= key**value
print(f'{itog} = ' + ' * '.join([f'{key}^{value}' for key, value in ans.items()]))


if any([itog % i != 0 for i in range(2, n + 1)]):
    print('Алгоритм говно')


