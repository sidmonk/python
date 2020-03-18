import random

A = [4, 8, 3, 1, 2, 1, 3, -1, 100]


def quick_sort(A):
    if len(A) < 2:
        return A
    else:
        # Выбираем случайный опорный элемент(pivot)
        i_pivot = random.randint(0, len(A) - 1)
        pivot = A[i_pivot]
        less = [i for i in A[: i_pivot] + A[i_pivot + 1:] if i < pivot]
        greater = [i for i in A[: i_pivot] + A[i_pivot + 1:] if i >= pivot]
        return quick_sort(less)  + [pivot] + quick_sort(greater)

print(quick_sort(A))