""" Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте
это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.
Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53)
является 938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков. Какова сумма очков имен в файле?"""

names = []
with open('22.txt') as f:
    for line in f:
        names += line.split(',')

for i in range(len(names)):
    names[i] = names[i][1: -1]

names.sort()

d = {}

for i in range(len(names)):
    d[names[i]] = i + 1

def alf_points(s):
    p = 0
    for i in str(s):
        p += (ord(i) - 64)
    return p


for i in d.keys():
    d[i] *= alf_points(i)

s = 0
for i in d.keys():
    s += d[i]
print(s)