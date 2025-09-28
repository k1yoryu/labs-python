user_input = input("Введите числа через пробел: ")
parts = user_input.split()

numbers = []

for part in parts:
    num = float(part)
    if num.is_integer():
        numbers.append(int(num))
    else:
        numbers.append(num)
print(numbers)
