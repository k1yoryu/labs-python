text = input("Введите строку: ")
if not text:
    print("Пустая строка!")
else:
    textlower = text.lower()
    if textlower == textlower[::-1]:
        print("Это палиндром")
    else:
        print("Это не палиндром")