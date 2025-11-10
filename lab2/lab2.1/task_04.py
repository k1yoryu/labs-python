user_input_1 = input("Введите 1-ый набор чисел: ")
parts1 = user_input_1.split()

list_1 = []
for part in parts1:
    value = float(part)
    if value.is_integer():
        list_1.append(int(value))
    else:
        list_1.append(value)

user_input_2 = input("Введите 2-ой набор чисел: ")
parts2 = user_input_2.split()

list_2 = []
for part in parts2:
    value = float(part)
    if value.is_integer():
        list_2.append(int(value))
    else:
        list_2.append(value)

set_1 = set(list_1)
set_2 = set(list_2)

vmeste = list(set_1 & set_2)
print("Общие числа: ", vmeste)

only_1 = list(set_1 - set_2)
print("Числа из первого набора, которых нет во втором: ", only_1)

only_2 = list(set_2 - set_1)
print("Числа из второго набора, которых нет в первом: ", only_2)

combined = list(set_1 ^ set_2)
print("Все числа, кроме общих: ", combined)
