def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < key:
            left = mid
        else:
            right = mid
    return left

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] <= key:
            left = mid
        else:
            right = mid
    return right

def bin_search(A, key):
    left = left_bound(A, key)
    right = right_bound(A, key)
    if right - left == 1:
        return left, right
    elif right - left == 2:
        return left + 1
    else:
        return left + 1, right - 1

A = [2, 3, 3, 7, 9, 10, 10, 12, 12]
key = 3
print(bin_search(A, key), left_bound(A, key), right_bound(A, key))