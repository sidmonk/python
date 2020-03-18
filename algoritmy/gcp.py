from random import randint

def len_gcs(A, B):
    """Возвращает длину наибольшей общей подпоследовательности"""
    lens = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]  #lens[i][j] = len_gcs(A[0:i], B[0:j])
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
    # чтобы убрать повторяющиеся подпоследовательности. Списки не могут быть элем. мн-ва. Поэтому лепим кортежи
    return list(set(tuple(j) for i in subs for j in i if len(j) == max_len))


def len_grand_incr_sub(A):
    lens = [0 for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        lens[i] = 1 + max(lens[j] if A[i-1] > A[j-1] else 0 for j in range(len(lens[:i])))
    return max(lens)

def grand_incr_sub(A):
    """Возвращает наибольшие возрастающие подпоследовательности"""
    # элемент списка - наибольшая подпоследовательность из A[:i], заканчивающаяся последним элементом среза
    grands = [[] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        # выбираем из всех ранее найденных подпоследовательностей ту, последний элемент которой меньше A[:i][-1]
        incrs = [j for j in grands[:i] if len(j) > 0 and j[-1] < A[i-1]]
        incrs.append([])    # для того, чтобы в мах не подать пустой список
        grands[i] = max(incrs, key=len) + [A[i-1]]  # находим из них макс по длине
    maxlen = max(len(i) for i in grands)
    return list(set([tuple(i) for i in grands if len(i) == maxlen]))    # возвращаем самые длинные и убираем повт.



def grand_incr_subs1(A):
    """Возвращает наибольшую возрастающую подпоследовательность. для неубывания убрать set"""
    return grand_common_subs(A, sorted(set(A)))



def grand_decr_subs1(A):
    """Возвращает наибольшую убывающую подпоследовательность. для невозрастания убрать set"""
    return grand_common_subs(A, sorted(set(A), reverse=True))


if __name__ == '__main__':
    A = [randint(0, 5) for i in range(8)]
    print(A)
    print(grand_incr_subs1(A))
    print(grand_incr_sub(A))
    print(grand_decr_subs1(A))
    B = [randint(0, 5) for i in range(8)]
    print(B)
    print(grand_common_subs(A, B))

