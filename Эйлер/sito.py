from datetime import *
from math import sqrt
from collections import Counter


def Erat(n):
    A = {2} | set(i for i in range(3, n + 1, 2))
    for p in range(3, int(sqrt(n) + 1), 2):
        d_e = p**2
        while d_e < n:
            A.discard(d_e)
            d_e += 2*p
    return A


def mnoj(n):
    d = {}
    while n % 2 == 0:
        n /= 2
        d[2] = d.get(2, 0) + 1
    i = 3
    while n != 1:
        if n % i == 0:
            n /= i
            d[i] = d.get(i, 0) + 1
            continue
        i += 2
    return d

def oldmnoj(n):
    A = sorted(Erat(n))
    mn = dict()
    for i in A:
        while n % i == 0:
            mn[i] = mn.get(i, 0) + 1
            n /= i
    return mn


def NOK(*args):
    resmn = dict()
    ans = 1
    for i in sorted(args):
        for key, value in mnoj(i).items():
            resmn[key] = max(resmn.get(key, 0), value)
    return resmn

def gcd(a, b):
    return a if b ==0 else gcd(b, a%b)

def max_s_del(n, s=4):
    i = 0
    max_simp = 1
    E = sorted(list(Erat(10**s)))
    while n != 1:
        while n % E[i] == 0:
            max_simp = max(max_simp, E[i])
            n /= E[i]
        i += 1
        if i > len(E) - 1:
            E = sorted(list(Erat(10 ** (s+1))))
    return max_simp


def n_simple(n):
    ss = [4, 25, 168, 1229, 9592, 78498, 664577, 10**9]
    s = min([i + 1 for i in range(len(ss)) if ss[i]>= n])
    if s == 8:
        return 'Эратосфен не прокатит'
    else:
        return sorted(Erat(10**s))[n-1]


def issimpleold(n):
    e = sorted(Erat(n))
    if n in e:
        return True
    else:
        return False

def issimple(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def simplenum(n):
    if issimple(n):
        return len(Erat(n))

def countdel(n):
    ans = 1
    for value in mnoj(n).values():
        ans *= value + 1
    return ans

def NOD(*args):
    razl = []
    for i in args:
        razl.append(Counter(mnoj(i)))
    ans = razl[0]
    for i in razl[1:]:
        ans &= i
    if len(ans) == 0:
        return 1
    else:
        return ans


def all_del(n):
    dic = mnoj(n)

    def rec(d):
        if len(d) == 0:
            return [1]
        else:
            current = list(d.keys())[-1]
            old_dict = dict([(key, value) for key, value in list(d.items())[:-1]])
            old_ans = rec(old_dict)
            new_ans = [i * current for i in old_ans]
            old_ans += new_ans
            for i in range(1, d[current]):
                new_ans = [i * current for i in new_ans]
                old_ans += new_ans
            return old_ans

    return rec(dic)

def chislo(d):
    ans = 1
    d[1] = 1
    for key, value in d.items():
        ans *= key**value
    return ans

def sokr(a, b):
    a = Counter(mnoj(a))
    b = Counter(mnoj(b))
    a, b = a - b, b - a
    return chislo(a), chislo(b)

def ankin(n):
    flag = [False for i in range(n + 1)]

    for i in range(int(sqrt(n)) + 1):
        for j in range(int(sqrt(n)) + 1):
            a = 4 * i ** 2 + j ** 2
            if a <= n and (a % 12 == 1 or a % 12 == 5):
                flag[a] = not flag[a]
            a -= i ** 2
            if a <= n and (a % 12 == 7):
                flag[a] = not flag[a]
            a -= 2 * j ** 2
            if i > j and a <= n and a % 12 == 11:
                flag[a] = not flag[a]

    for i in range(5, int(sqrt(n)) + 1):
        if flag[i]:
            p = i ** 2
            k = p
            while k <= n:
                flag[k] = False
                k += p
    flag[1] = False
    flag[2] = True
    flag[3] = True
    simp = set()
    for i in range(n + 1):
        if flag[i]:
            simp.add(i)
    return simp


if __name__ == '__main__':
    start_time = datetime.now()
    print(issimple(19134702400093278081449423917))
    end_time = datetime.now()
    print(f'Duration: {end_time - start_time}')





