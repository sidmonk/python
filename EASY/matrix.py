a = []
r = 0
while True:
    t = input()
    if t == 'end':
        break
    r += 1
    a.append([int(i) for i in t.split()])

c = len(a[0])

if c == 1 and r == 1:
    b = 4*a[0][0]
    print(b)
    exit()

b = []
for i in range(r):
    b.append([0] * c)

for i in range(r-1):
    for j in range(c-1):
        b[i][j] = a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1]

for j in range(c-1):
    b[r-1][j] = a[r-2][j]+a[0][j]+a[r-1][j-1]+a[r-1][j+1]

for i in range(r-1):
    b[i][c-1] = a[i][c-2]+a[i][0]+a[i-1][c-1]+a[i+1][c-1]

b[r-1][c-1] = a[r-2][c-1]+a[0][c-1]+a[r-1][c-2]+a[r-1][0]

for row in b:
    for elem in row:
        print(elem, end=' ')
    print()



