import random

random_chislo = random.randint(1, 100)
otvet = 0

print("Угадай число от 1 до 100")
while otvet != random_chislo:
    otvet = int(input("Ваш вариант: "))

    if otvet < random_chislo:
        print("Больше")
    elif otvet > random_chislo:
        print("Меньше")
    else:
        print("Угадал! Загаданное число: ", random_chislo)