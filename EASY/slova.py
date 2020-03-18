n = int(input())
d = {}
for i in range(n):
    s1 = input().lower()
    if s1 not in d.keys():
        d[s1] = 0
s = []
n = int(input())
for i in range(n):
    s += input().lower().split()

d1 = {}
for i in s:
    if i not in d.keys():
        d1[i] = 1

for key in d1.keys():
    print(key)