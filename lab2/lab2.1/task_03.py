user_input = input("Введите числа через пробел: ")
parts = user_input.split()

numbers = []

for part in parts:
    value = float(part)
    if value.is_integer():
        numbers.append(int(value))
    else:
        numbers.append(value)

numbers.sort(reverse=True)
print("Список от большего к меньшему: ", numbers)
print("Второе по величине число: ", numbers[1])