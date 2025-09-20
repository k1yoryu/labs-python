stroka = input("Введите строку: ")

if not stroka:
    print("Ошибка: строка не должна быть пустой!")
else:
    glasnie = "aeiou"
    result = ""

    for char in stroka:
        if char.lower() not in glasnie:
            result += char

    print("Результат:", result)
