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

vmeste = []
for num in list_1:
    if num in list_2 and num not in vmeste:
        vmeste.append(num)
print("Общие числа: ", vmeste)

only_1 = []
for num in list_1:
    if num not in list_2 and num not in only_1:
        only_1.append(num)
print("Числа из первого набора, которых нет во втором: ", only_1)

only_2 = []
for num in list_2:
    if num not in list_1 and num not in only_2:
        only_2.append(num)
print("Числа из второго набора, которых нет в первом: ", only_2)

combined = []
for num in list_1 + list_2:
    if num not in vmeste and num not in combined:
        combined.append(num)
print("Все числа, кроме общих: ", combined)