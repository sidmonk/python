'''f = open('games.txt')
n = int(f.readline())
s = []
for i in range(n):
    s += [f.readline().strip()]
f.close()'''
n = int(input())
s = []
for i in range(n):
    s += [input()]
g = []
m = ''

for i in range(len(s)):
    m = s[i]
    g += [m.split(';')]

t = {}
for i in range(n):
    if g[i][0] in t.keys():
        t[g[i][0]][0] += 1
    else:
        t[g[i][0]] = [1]
    if g[i][2] in t.keys():
        t[g[i][2]][0] += 1
    else:
        t[g[i][2]] = [1]

for i in t.keys():
    t[i] += 4*[0]

for i in range(n):
    if int(g[i][1]) > int(g[i][3]):
        t[g[i][0]][1] += 1
        t[g[i][0]][4] += 3
        t[g[i][2]][3] += 1
    elif int(g[i][1]) < int(g[i][3]):
        t[g[i][2]][1] += 1
        t[g[i][2]][4] += 3
        t[g[i][0]][3] += 1
    if int(g[i][1]) == int(g[i][3]):
        t[g[i][0]][2] += 1
        t[g[i][0]][4] += 1
        t[g[i][2]][2] += 1
        t[g[i][2]][4] += 1

for key in t.keys():
    print(key+':', end='')
    for i in range(5):
        print(t[key][i], end=' ')
    print()
