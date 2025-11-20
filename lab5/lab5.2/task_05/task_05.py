def combine_dicts(dict_a, dict_b):
    for key, value in dict_b.items():
        if key in dict_a:
            if isinstance(dict_a[key], dict) and isinstance(value, dict):
                combine_dicts(dict_a[key], value)
            elif isinstance(dict_a[key], list) and isinstance(value, list):
                dict_a[key].extend(value)
            elif isinstance(dict_a[key], set) and isinstance(value, set):
                dict_a[key].update(value)
            else:
                dict_a[key] = value
        else:
            dict_a[key] = value