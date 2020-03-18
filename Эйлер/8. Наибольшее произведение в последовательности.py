'''
Наибольшее произведение четырех последовательных цифр в нижеприведенном 1000-значном числе равно 9 × 9 × 8 × 9 = 5832.
Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.
'''

s = ''
with open('8.TXT') as f:
    for line in f:
        s += line

n = 13
c = 1
maxpr = 1
i = 0
while i < len(s) - n:
    c = 1
    s1 = s[i: i + n]
    if s1.rfind('0') != -1:
        i += s1.rfind('0') + 1
        continue
    for j in s1:
        c *= int(j)
    maxpr = max(c, maxpr)
    i += 1


print(maxpr)


