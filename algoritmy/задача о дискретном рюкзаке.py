items = [(2, 3), (3, 4), (5, 6)]
masses = [2, 3, 4]
costs = [3, 4, 6]

def backpack(masses: list, costs: list, limit: int)  -> int:
    backpacks = [[0]*(limit+1) for i in range(len(masses)+1)]
    for i in range(1, len(backpacks)):
        for j in range(1, limit+1):
            if j >= masses[i-1]:
                backpacks[i][j] = max(backpacks[i-1][j], backpacks[i-1][j - masses[i-1]] + costs[i-1])
            else:
                backpacks[i][j] = backpacks[i-1][j]
    return backpacks[-1][-1]

print()
