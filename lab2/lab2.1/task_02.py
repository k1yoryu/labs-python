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

povtor_numbers = []

for num in numbers:
    if numbers.count(num) > 1:
        if num not in povtor_numbers:
            povtor_numbers.append(num)
print("Повторяющиеся числа: ", *povtor_numbers)

chetnie_numbers = []
nechetnie_numbers = []

for num in numbers:
    if num % 1 == 0:
        if num % 2 == 0:
            if num not in chetnie_numbers:
                chetnie_numbers.append(num)
        else:
            if num not in nechetnie_numbers:
               nechetnie_numbers.append(num)
print("Чётные числа: ", *chetnie_numbers)
print("Нечётные числа: ", *nechetnie_numbers)

otricatelnie_numbers = []
for num in numbers:
    if num < 0:
        if num not in otricatelnie_numbers:
            otricatelnie_numbers.append(num)
print("Отрицательные числа: ", *otricatelnie_numbers)

float_numbers = []
for num in numbers:
    if num % 1 != 0:
        if num not in float_numbers:
            float_numbers.append(num)
print("Числа с плавающей точкой: ", *float_numbers)

sum_kr_5 = 0
for num in numbers:
    if num % 5 == 0:
        sum_kr_5 += num
print("Сумма чисел, кратных 5: ", sum_kr_5)

max_number = max(numbers)
print("Самое большое число: ", max_number)

min_number = min(numbers)
print("Самое маленькое число: ", min_number)
