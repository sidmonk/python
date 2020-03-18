
costs['D'] = inf
costs['fin'] = inf

parents = {}
parents['start'] = ''
parents['A'] = 'start'
parents['B'] = 'start'


processed = []

import collections

graphs = {}

graphs['start'] = {'A': 5, 'B': 2}
graphs['A'] = {'C': 4, 'D': 2}
graphs['B'] = {'D': 7, 'A': 8}
graphs['C'] = {'fin': 3, 'D': 6}
graphs['D'] = {'fin': 1}
graphs['fin'] = {}

inf = float('inf')
costs = {}
costs['start'] = 0
costs['A'] = 5
costs['B'] = 2
costs['C'] = inf


def find_lowest_cost_node():
    lowest_cost = inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
            return lowest_cost_node
    return None
node = find_lowest_cost_node()

while node is not None:
    neighbors = graphs[node]
    cost = costs[node]
    for neighbor in neighbors:
        new_cost = cost + graphs[node][neighbor]
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed += [node]
    node = find_lowest_cost_node()

way = 'fin'
node = 'fin'
while node != '':
    node = parents[node]
    way = node + ' ' + way

print(way[1: ])
print(costs['fin'])