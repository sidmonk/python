n = int(input())
a = []
b = []
for i in range(n):
    a.append([0] * n)

for i in range(1, n**2 + 1):
    b += [i]
s = 0
i = 0
j = -1

while s < n**2:
    while True:
        if j+1 > n-1:
            break
        if a[i][j+1] in b :
            break
        j += 1
        a[i][j] = b[s]
        s += 1
    while True:
        if i+1 > n-1:
            break
        if a[i+1][j] in b :
            break
        i += 1
        a[i][j] = b[s]
        s += 1
    while True:
        if j == 0:
            break
        if a[i][j-1] in b :
            break
        j -= 1
        a[i][j] = b[s]
        s += 1
    while True:
        if a[i-1][j] in b :
            break
        i -= 1
        a[i][j] = b[s]
        s += 1

for row in a:
    for elem in row:
        print(str(elem).ljust(4), end='')
    print()