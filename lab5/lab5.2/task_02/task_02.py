def find_unique(input_list):
    result = []
    if not input_list:
        return []
    for item in input_list:
        if input_list.count(item) == 1:
            result.append(item)
    return result