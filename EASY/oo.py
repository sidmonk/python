with open('dataset_3380_5.txt', encoding='utf-8') as f:
    s = f.read().splitlines()

d = {i: [0, 0] for i in range(1, 12)}
print(s)
for i in range(len(s)):
    s1 = s[i].split('\t')
    if int(s1[0]) in d.keys():
        d[int(s1[0])][0] += int(s1[2])
        d[int(s1[0])][1] += 1
for i in range(1, 12):
    print(i, end=' ')
    if d[i][1] == 0:
        print('-')
    else:
        print(d[i][0] / d[i][1])