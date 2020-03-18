import pickle
import persona


d = dict(x = '2')
with open('db1.txt', 'wb') as f:    #w - write, b - bytes
    pickle.dump(d, f)

with open('db1.txt', 'rb') as f:    #r - read
    d1 = pickle.load(f)

print(d1)


import shelve

with shelve.open('db2') as db2:
    db2['Gnoiny'] = 'pidor'

with shelve.open('db2') as db2:
    print(db2['Gnoiny'])

d = {}
with shelve.open('per') as per:
    for key in per.keys():
       per[key].name

a = persona.Person('Anya')
print(a)