import collections
s = input().lower().split()
d = {}
for i in range(len((s))):
    if s[i] in d.keys():
        d[s[i]] += 1
    else: d[s[i]] = 1
