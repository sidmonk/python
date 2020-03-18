z = input()
r = input()
z1 = input()
r1 = input()
d1 = {}
for i in range(len(z)):
    d1[z[i]] = r[i]

d2 = {}
for i in range(len(z)):
    d2[r[i]] = z[i]

z2 = ''
for i in range(len(z1)):
    if z1[i] in d1.keys():
        z2 += d1[z1[i]]
    else:
        z2 += z1[i]

r2 = ''
for i in range(len(r1)):
    if r1[i] in d2.keys():
        r2 += d2[r1[i]]
    else:
        r2 += r1[i]

print(z2)
print(r2)