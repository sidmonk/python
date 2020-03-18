a, b = (int(i) for i in input().split())
s = 0
c = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        c += 1
    i += 1
print (s / c)