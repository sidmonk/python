n = 6
for i in range(2**(n-1)):
    print(bin(i)[2:].ljust(n, '0'))
