stroka = input("Введите строку: ")

if not stroka:
    print("Ошибка: строка не должна быть пустой!")
else:
    result = stroka.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "") \
                   .replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    print("Результат:", result)
