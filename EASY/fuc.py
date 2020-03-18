lst = [int(i) for i in input().split()]
def modify_list(lst):
    i = 0
    while True:
        if i >= len(lst):
            break
        if lst[i] % 2 == 1:
            lst.remove(lst[i])
            continue
        if lst[i] % 2 == 0:
            lst[i] = int(lst[i]/2)
        i += 1
modify_list(lst)
for i in lst:
    print(i, end=' ')