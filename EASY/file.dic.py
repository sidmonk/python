f = open('dataset_3363_3.txt', 'r')
s = f.read()
f.close()
print(s)

d = {}
for i in s.lower().split():
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

m = max(d.values())
w = []
for i in d.keys():
    if d[i] == m:
        w += [i]

w.sort()
print(w[0], m)
