s = input()
j = 1
cs = ''
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        j += 1
    else:
        cs = cs + s[i - 1] + str(j)
        j = 1
cs = cs + s[-1] + str(j)
print(cs)