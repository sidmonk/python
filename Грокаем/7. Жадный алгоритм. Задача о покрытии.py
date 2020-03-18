stations = {}
stations["kone"]  = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

states_needed = set.union(*stations.values())
choise = set()

while states_needed:
    best_station = None
    best_covered = set()
    for station, states in stations.items():
        covered = set.intersection(states_needed, states)
        if len(covered) > len(best_covered):
            best_station = station
            best_covered = covered
        states_needed -= best_covered
        choise.add(best_station)

print(choise)