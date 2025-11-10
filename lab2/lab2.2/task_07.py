def merge_sorted_list(list1, list2):
    i, j = 0, 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

input1 = input("Введите первый отсортированный список (через пробел числа): ")
input2 = input("Введите второй отсортированный список: (через пробел числа) ")

list1 = [int(x) for x in input1.split()]
list2 = [int(x) for x in input2.split()]

result = merge_sorted_list(list1, list2)
print("Результат слияния:", *result)