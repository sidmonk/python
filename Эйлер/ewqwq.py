import sito
import datetime

def newmnoj(n):
    d = {}
    while n % 2 == 0:
        n /= 2
        d[2] = d.get(2, 0) + 1
    i = 3
    while n != 1:
        while n % i == 0:
            n /= i
            d[i] = d.get(i, 0) + 1
        i += 2
    return d

t1 = datetime.datetime.now()
print(sito.mnoj(28341341))
t2 = datetime.datetime.now()

print(t2 - t1)

t1 = datetime.datetime.now()
print(newmnoj(28341341))
t2 = datetime.datetime.now()
print(t2 - t1)
