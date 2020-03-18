'''Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр.'''

def period(n):
    # Эта фффункция выводит остаток, если он есть, если нету, то ноль
    ost = 1
    osts = []
    rezs = []
    answ = ''
    per = ''
    while True:
        ost *= 10
        rez = ost // n
        ost = ost % n
        if ost == 0:
            return 0
        if ost in osts and rez in rezs:
            b = len(osts) - 1 - osts[:: -1].index(ost)
            # Эта дрочь нужна чтобы вывести полностью число, а не остаток
            # for i in rezs[0: b]:
            #     answ += str(i)
            for i in rezs[b: ]:
                per += str(i)
            return int(per)
        osts += [ost]
        rezs += [rez]

d_max = 0
per_max = 0

for d in range(3, 1000):
    curr_per = period(d)
    if curr_per > per_max:
        per_max = curr_per
        d_max = d

print(d_max, per_max)

