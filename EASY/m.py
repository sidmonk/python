a = [int(i) for i in input().split()]
b = []
if len(a) == 1:
    b += [a[0]]
    print(b[0])
    exit()
for i in range(0, len(a)):
    if i == len(a) - 1:
        b += [a[i - 1] + a[0]]
        continue
    b += [a[i - 1] + a[i + 1]]
for i in b:
    print(i , end = ' ')