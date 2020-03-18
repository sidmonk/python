def findu(s):
    u = set()
    for i in range(len(s)):
        if ord(s[i]) in range(65, 90):
            u.add(i)
    return(u)

from collections import defaultdict
d = defaultdict(set)
for i in range(int(input())):
    s = input()
    d[s.lower()] |= findu(s)

n = 0
hw = input().split()
for h in hw:
    if len(findu(h)) == len(h) and len(h) != 1:
        continue
    elif (h.lower() in d.keys() and len(d[h.lower()] & findu(h)) >= 1) or (h.lower() not in d.keys() and len(findu(h)) == 1):
        n += 1

print(len(hw) - n)