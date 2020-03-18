from random import randint

def len_gcs(A, B):
    """Возвращает длину наибольшей общей подпоследовательности"""
    lens = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                lens[i][j] = 1 + lens[i-1][j-1]
            else:
                lens[i][j] = max(lens[i-1][j], lens[i][j-1])
    return lens[-1][-1]

def grand_common_subs(A, B):
    """Возвращает наибольшие общие подпоследовательности двух последовательностей"""
    subs = [[[] for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                subs[i][j] = subs[i-1][j-1] + [A[i-1]]
            else:
                subs[i][j] = max(subs[i-1][j], subs[i][j-1], key=len)
    max_len = len_gcs(A, B)
    return list(set(tuple(j) for i in subs for j in i if len(j) == max_len))


def len_grand_incr_sub(A):
    lens = [0 for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        lens[i] = 1 + max(lens[j] if A[i-1] > A[j-1] else 0 for j in range(len(lens[:i])))
    return max(lens)

def grand_incr_sub(A):
    """Возвращает наибольшие возрастающие подпоследовательности"""
    grands = [[] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        a = [j if len(j) > 0 and j[-1] < A[i-1] else [] for j in grands[:i]]
        grands[i] = max(a, key=len) + [A[i-1]]
    maxlen = max(len(i) for i in grands)
    return list(set([tuple(i) for i in grands if len(i) == maxlen]))



def grand_incr_subs1(A):
    """Возвращает наибольшую возрастающую подпоследовательность"""
    return grand_common_subs(A, sorted(A))



def grand_decr_subs(A):
    """Возвращает наибольшую возрастающую подпоследовательность"""
    return grand_common_subs(A, sorted(A, reverse=True))


if __name__ == '__main__':
    A = [randint(0, 5) for i in range(8)]
    print(A)
    print(len_grand_incr_sub(A))
    print(grand_incr_sub(A))
    B = [randint(0, 5) for i in range(8)]
    print(B)
    print(grand_common_subs(A, B))

