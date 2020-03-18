M = [[False, True, True, False, False],
     [True, False, True, False, False],
     [True, True, False, True, False],
     [False, False, True, False, False],
     [False, False, False, False, False]]
n = len(M)

def cycle(M):
    ways = []
    for start in range(n):
        for j in range(n):
            if M[start][j]:
                ways.append(str(start) + str(j))
        while ways:
            way = ways.pop()
            for j in range(n):
                if M[int(way[-1])][j] and j != int(way[-2]):
                    new_way = way + str(j)
                    if any([new_way[-1] == i for i in way]):
                        return True
                    else:
                        ways.append(new_way)
    return False

print(cycle(M))
