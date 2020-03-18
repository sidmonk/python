with open('dataset_3363_4.txt', 'r') as f:
    a = f.read().splitlines()

d = {}

for i in a:
    s = i.split(';')
    d[s[0]] = [int(s[1])]
    d[s[0]] += [int(s[2])]
    d[s[0]] += [int(s[3])]
s1 = 0
avg = []
avg1 = []
l = 0
for key in d.keys():
    l = len(d[key])
    for j in range(len(d[key])):
        s1 += d[key][j]
    avg += [s1/3]
    s1 = 0

for j in range(l):
    for key in d.keys():
        s1 += d[key][j]
    avg1 += [s1/len(d)]
    s1 = 0
print(d)
print(avg)
print(avg1)

f = open('marks1.txt', 'w')
for i in avg:
   f.write(str(i) + '\n')
for i in avg1:
   f.write(str(i) + ' ')
f.close()
