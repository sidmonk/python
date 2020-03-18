a = [int(i) for i in input().split()]
i = 0
b = []
a.sort()
for i in range(len(a)):
    if a.count(a[i]) > 1 and a[i] not in b:
        b += [a[i]]
for i in b:
    print(i, end = ' ')
