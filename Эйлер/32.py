from sito import *
import datetime

n = 12345678
t1 = datetime.datetime.now()
print(len(Erat(n)))
t2 = datetime.datetime.now()
print(t2-t1)

t1 = datetime.datetime.now()
print(len(ankin(n)))
t2 = datetime.datetime.now()
print(t2-t1)