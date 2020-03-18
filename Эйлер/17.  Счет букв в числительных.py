'''Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?'''
d = {0: '',1:'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
     14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'ninteen'
     }

for i in range(20, 30):
    d[i] = 'twenty' + d[int(str(i)[1])]

for i in range(30, 40):
    d[i] = 'thirty' + d[int(str(i)[1])]

for i in range(40, 50):
    d[i] = 'fourty' + d[int(str(i)[1])]

for i in range(50, 60):
    d[i] = 'fifty' + d[int(str(i)[1])]

for i in range(60, 70):
    d[i] = 'sixty' + d[int(str(i)[1])]

for i in range(70, 80):
    d[i] = 'seventy' + d[int(str(i)[1])]

for i in range(80, 90):
    d[i] = 'eighty' + d[int(str(i)[1])]

for i in range(90, 100):
    d[i] = 'ninety' + d[int(str(i)[1])]

d1 = {}
for i in range(100, 1000):
    if i % 100 == 0:
        d[i] = d[int(str(i)[0])] + 'hundred' + d[int(str(i)[1:])]
    else:
        d[i] = d[int(str(i)[0])] + 'hundred' + 'and' + d[int(str(i)[1:])]
d[1000] = 'onethousand'

s = 0
for i in d.keys():
    s += len(d[i])

print(s)
