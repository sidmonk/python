def generate_numbers(M, N=10):
    """Генерирует все возможные чиcла длины M в N-ричной (N<=10) системе с лидирующими незначащими нулями.
       На выходе - список строк"""
    if N > 10:
        return 'На такое мы не способны'
    numbers = []

    def generator(M, N, prefix=None):
        prefix = prefix or []
        if M == 0:
            numbers.append(''.join([str(i) for i in prefix]))
        else:
            for i in range(N):
                generator(M-1, N, prefix+[i])

    generator(M, N)
    return numbers


def generate_accommodations(n=10, k=-1):
    """Генерирует все возможные размещния чисел от 0 до n-1 (n<=10) длины k. На выходе - список строк"""
    if n > 10:
        return 'На такое мы не способны'
    k = n if k == -1 or k > n else k
    numbers = []

    def generator(k, n, prefix=None):
        prefix = prefix or []
        if k == 0:
            numbers.append(' '.join([str(i) for i in prefix]))
        else:
            for i in range(n):
                if i in prefix:
                    continue
                generator(k-1, n, prefix+[i])

    generator(k, n)
    return numbers


def generate_list_accomodations(l, k=-1):
    """Генерирует все возможные перестановки в списке. На выходе - список строк"""
    l = sorted(list(l))
    n = len(l)
    k = n if k == -1 or k > n else k
    permutations = []

    def generator(l, k, prefix=None):
        prefix = prefix or []
        if k == 0:
            permutations.append(' '.join([str(i) for i in prefix]))
        else:
            for i in l:
                if i in prefix:
                    continue
                generator(l, k-1, prefix+[i])

    generator(l, k)
    return permutations

def generate_list_countings(l, k=-1):
    l = sorted(list(l))
    n = len(l)
    k = n if k == -1 or k > n else k
    countings = set([' '.join(sorted(list(set(i.replace(' ', ''))))) for i in generate_list_accomodations(l, k)])
    return sorted(list(countings))

print(generate_list_accomodations('abcd', 4))