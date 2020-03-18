'''Рассмотрим квадратичную формулу вида: n^2 +an+ b, где |a| <1000 и |b| ≤ 1000

Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное количество
простых чисел для последовательных значений n, начиная со значения n = 0.'''

# Используем сито Эратосфена для получения множества простых чисел простых чисел

k = 1000000
def eratosthenes(k):
    numbers = [i for i in range(k + 1)]
    p = 2
    while p**2 < k:
        for i in range(2*p, k + 1, p):
            numbers[i] = 0
        while True:
            p += 1
            if numbers[p] != 0:
                break
    prime_numbers = set(numbers) - {0}
    return prime_numbers

prime_numbers = eratosthenes(k)

max_count = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        count = 0
        n = 0
        for n in range(100):
            prime = n**2 + a*n + b
            if prime in prime_numbers:
                count += 1
                if count > max_count:
                    max_count = count
                    a_max = a
                    b_max = b
            else:
                break
            n += 1


print(max_count - 1, f'a_max = {a_max}', f'b_max = {b_max}', f'a*b = {a*b}', sep='\n')
