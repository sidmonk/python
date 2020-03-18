from random import randint
A = [randint(0, 10) for i in range(5)]


def merge(A, B):
    C = []
    i = j = 0
    while i < len(A)  and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C += A[i:] + B[j:]
    return C

def merge_sort(A:list):
    if len(A) <= 1:
        return A
    m = len(A)//2
    return merge(merge_sort(A[:m]), merge_sort(A[m:]))

print(merge_sort(A))