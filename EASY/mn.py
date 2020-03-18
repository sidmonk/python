d = {}
def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] = [value]
    elif key * 2 in d.keys():
        d[key*2] = [value]
    else: d[key*2] = [value]
    return(d)

update_dictionary(d, 8, 3)
print(d[16])