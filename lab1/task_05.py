number = int(input("Введите число: "))

if number % 7 == 0:
    result = "Магическое число!"
else:
    if number < 10:
        result = number
    elif number < 100:
        result = (number // 10) + number % 10
    elif number < 1000:
        result = (number // 100) + (number // 10) % 10 + number % 10
    elif number < 10000:
        result = (number // 1000) + (number // 100) % 10 + (number // 10) % 10 + number % 10
    else:
        result = "Слишком большое число!"

print(result)
