# сгенерировать какую-нибудь структуру (список с номерами автомобилей пару штук)
# 4 цифры 2 буквы - 1 цифра (от 1 до 8)
# пользователь вводит какой-то номер, автомобильный (либо формат прописать в принте)
# если находим в своем списке, то выводим, что такой номер уже есть

import random

def generate_number_plate():
    bukvi = 'ABCEHKMOPTX'

    first_digit_4 = random.randint(1000, 9999)
    bukva_1 = random.choice(bukvi)
    bukva_2 = random.choice(bukvi)
    region = random.randint(1, 8)

    return f"{first_digit_4} {bukva_1}{bukva_2} {region}"

plate_list = [generate_number_plate() for _ in range(5)]

print("Сгенерированные автомобильные номера:")
print(*plate_list, sep='\n')
print("\nФормат ввода номера: 1234 AB 5")
user_input = input("Введите автомобильный номер: ").strip()

if user_input in plate_list:
    print("Такой номер уже есть в списке!")
else:
    plate_list.append(user_input)
    print("Номер добавлен в список.")
    print(f"Теперь в списке {len(plate_list)} номеров.")


print("Обновленный список номеров: ")
print(*plate_list, sep='\n')