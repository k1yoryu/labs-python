def unique_elements(lst, result=None):

    if result is None:
        result = []

    for item in lst:
        if isinstance(item, list):
            unique_elements(item, result)
        else:
            if item not in result:
                result.append(item)

    return result

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
print("Исходный список:", list_a)
print("Уникальные элементы:", unique_elements(list_a))
