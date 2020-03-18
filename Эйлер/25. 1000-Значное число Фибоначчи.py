a = 0
b = 1
n = 1

while True:
    b, a = a + b, b
    n += 1
    if len(str(b)) >= 1000:
        break

print(n)