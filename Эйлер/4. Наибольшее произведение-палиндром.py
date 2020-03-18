'''
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
'''

start = 100
finish = 1000

def maxpol(start, finish):
    max = 0
    for i in range(start, finish + 1):
        for j in range(i, finish + 1):
            pr = i * j
            if str(pr) == str(pr)[::-1] and pr > max:
                max = pr
                imax, jmax = i, j
    return imax, jmax, max

ans = maxpol(start, finish)
print('{}*{} = {}'.format(*ans))

