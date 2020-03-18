from collections import deque

def is_seller(name):
    if len(name) > 5:
        return True
    else:
        return False

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

searched = []

search_queqe = deque()
search_queqe += graph['you']
while search_queqe:
    person = search_queqe.popleft()
    if person not in searched:
        if is_seller(person):
            print(f'{person} is seller')
            break
        else:
            search_queqe += graph[person]
            searched += [person]