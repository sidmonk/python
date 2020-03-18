d = {}
for i in range(int(input())):
    d[input()] = 0
n = 0

def ucount(s):
    n = 0
    for i in range(len(s)):
        if ord(s[i]) in range(65, 90):
            n += 1
    return(n)

def somew(s):
    sw = []
    n = 0
    if ucount(s) > 1:
        for i in range(len(s)):
             if ord(s[i]) in range(65, 90):
                sw += [s[: i].lower() + s[i] + s[i+1: ].lower()]
        return(tuple(sw))
    else:
        return(s)


n = 0
s = input().split()
for i in s:
    for j in somew(i):
        if j in d.keys():
            n += 1
            continue
        elif j.isupper() == 'True' and len(j) == 1:
            n += 1
        elif j not in d.keys() and ucount(j) == 1:
            n += 1

print(len(s) - n)

