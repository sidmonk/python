n = int(input())
n1 = n

if n >= 100:
    n %= 100

if n > 14:
    n %= 10

if n == 1:
    print(n1, 'программист')
elif n in [2, 3, 4]:
    print(n1, 'программиста')
elif n in [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
    print(n1, 'программистов')

