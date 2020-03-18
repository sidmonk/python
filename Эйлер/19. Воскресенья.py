'''Дана следующая информация (однако, вы можете проверить ее самостоятельно):

1 января 1900 года - понедельник.
В апреле, июне, сентябре и ноябре 30 дней.
В феврале 28 дней, в високосный год - 29.
В остальных месяцах по 31 дню.
Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00) является високосным в том и только том случае, если делится на 400.
Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?'''

import collections
n = 0
i = 1
D = []
date = collections.namedtuple('date', 'd m y w')
lowanydaym = (4, 6,  9, 11)
for year in range(1901, 2001):
    for month in range(1, 13):
        if month in lowanydaym:
            max_day = 30
        elif month == 2:
            if year % 4 == 0 and year % 100 != 0:
                max_day = 29
            else:
                max_day = 28
        else:
            max_day = 31
        for day in range(1, max_day + 1):
            i += 1
            if i % 8 == 0:
                i = 1
            date1 = date(day, month, year, i)
            date_ = date1
            d = date_
            if d.d == 1 and d.w == 7:

                n += 1
print(n)