surname = input("Введите фамилию: ")
name = input("Введите имя: ")
otchestvo = input("Введите отчество: ")

if not surname or not name or not otchestvo:
    print("Ошибка: все поля должны быть заполнены!")
else:
    result = surname + " " + name[0] + "." + otchestvo[0] + "."
    print("Результат:", result)