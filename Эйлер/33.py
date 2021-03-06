"""Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее, будет ошибочно полагать,
 что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.
Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.

Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и содержат двухзначные числа как
в числителе, так и в знаменателе.
Пусть произведение этих четырех дробей дано в виде несократимой дроби
 (числитель и знаменатель дроби не имеют общих сомножителей). Найдите знаменатель этой дроби."""

import sito

A = []
for i in range(10, 100):
    for j in range(10, 100):
        i1 = str(i)
        j1 = str(j)
        s1, s2 = sito.sokr(i, j)
        if i1[1] == j1[0]:
            i1 = int(i1[0])
            j1 = int(j1[1])
            i1, j1 = sito.sokr(i1, j1)
            if i1 == s1 and j1 == s2:
                A.append((i1, j1))
                print(i1, j1)
print(A)