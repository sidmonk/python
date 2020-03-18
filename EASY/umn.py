a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('  ', end = '')
for j in range(c, d + 1):
    print(j, end = ' ')
print()

for i in range(a, b + 1):
    print(i, end=' ' )
    for j in range(c, d + 1):
        print(i * j, end = ' ')
    print()

