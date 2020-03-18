A = [1, 2, 3, 4, 5]

def bin_find(A, a):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = int(l + r) // 2
        guess = A[m]
        if a > guess:
            l = m + 1
        elif a == guess:
            return m
        else:
            r = m - 1
    return None

print(bin_find(A, 4))