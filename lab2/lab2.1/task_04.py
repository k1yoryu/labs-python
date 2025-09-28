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