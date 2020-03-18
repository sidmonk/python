f = open('dataset_3363_3', 'r')
s = f.read()
f.close()
print(s)

b = []
c = []
i = 0
s1 = ''

while i < len(s):
    if '0' <= s[i] <= '9':
        b += [s[i-1]]
        if i + 1 == len(s):
            break
        if '0' <= s[i + 1] <= '9':
            c.append(s[i] + s[i + 1])
            i += 1
        else:
            c += s[i]
    i += 1

if '0' <= s[-2] <= '9':
    c.append(s[-1] + s[-2])
else:
    c += s[-1]

for i in range(len(b)):
    s1 += b[i]*int(c[i])
print(s1)

f = open('file.txt', 'w')
f.write(s + '\n')
f.write(s1)
f.close()

