def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] = [value]
    elif key not in d.keys():
        d[2 * key] = [value]