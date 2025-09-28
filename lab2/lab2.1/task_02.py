user_input = input("Введите числа через пробел: ")
parts = user_input.split()

numbers = []

for part in parts:
    value = float(part)
    if value.is_integer():
        numbers.append(int(value))
    else:
        numbers.append(value)
print(numbers)

unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)
print("Уникальные числа: ", *unique_numbers)

