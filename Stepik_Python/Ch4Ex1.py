def update_dictionary(d, key, value):
    if key in d.keys():
        d.get(key).append(value)
    elif key*2 in d.keys():
        d.get(key*2).append(value)
    else:
        d[2 * key] = [value]

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
