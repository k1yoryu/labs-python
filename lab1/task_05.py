number = int(input("Введите число: "))
if number % 7 == 0:
    print("Магическое число!")
else:
    summa = 0
    while number > 0:
        cifra = number % 10
        summa += cifra
        number = number // 10
    print(summa)