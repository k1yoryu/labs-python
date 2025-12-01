# класс автобус, содержит следующие свойства: скорость, максимальная вместимость пассажиров, максимальная скорость,
# наличие свободных мест. Методы: посадка / высадка одного или нескольких пассажиров, увеличение или уменьшение скорости
# на заданное значение (через пользовательский ввод). Должно быть пользовательское исключение (для скорости, допустим выше максимальной пытаемся
# ввести, например, скорость и хотят уменьшить на 50, то ошибка через собственное исключение)

class SpeedError(Exception):
    pass

class PersonError(Exception):
    pass

class Bus:
    def __init__(self, velocity, max_person, max_velocity):
        self.velocity = velocity
        self.max_person = max_person
        self.max_velocity = max_velocity
        self.persons = 0
        self.free_places = max_person

    def posadka_person(self, person):
        if person <= 0:
            raise PersonError("число должно быть положительным")
        if self.persons + person > self.max_person:
            print("Мест нет.")
        else:
            self.persons += person
            self.free_places -= person
            print(f"Посажено {person} пассажиров. Свободных мест: {self.free_places}")

    def visodka_person(self, person):
        if person <= 0:
            raise PersonError("количество должно быть положительным")
        if person > self.persons:
            raise PersonError("нельзя высадить больше пассажиров, чем есть в автобусе")
        else:
            self.persons -= person
            self.free_places += person
            print(f"Высажено {person} пассажиров. Свободных мест: {self.free_places}")

    def speed_up(self, value):
        if value < 0:
            raise SpeedError("скорость не может быть отрицательной")
        if self.velocity + value > self.max_velocity:
            raise SpeedError(f"увеличение на {value} превысит максимальную ({self.max_velocity})")
        self.velocity += value
        print(f"Скорость увеличена. Текущая скорость: {self.velocity} км/ч")

    def speed_down(self, value):
        if value < 0:
            raise SpeedError("скорость не может быть отрицательной")
        if self.velocity - value < 0:
            raise SpeedError("скорость не может быть меньше 0.")
        self.velocity -= value
        print(f"Скорость уменьшена. Текущая скорость: {self.velocity} км/ч")

def main():
    bus = Bus(velocity=0, max_person=40, max_velocity=180)

    while True:
        print("\nАвтобус (...Здравствуй небо в облаках...)")
        print("1. Посадить пассажиров")
        print("2. Высадить пассажиров")
        print("3. Увеличить скорость")
        print("4. Уменьшить скорость")
        print("5. Состояние автобуса")
        print("6. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':
                n = int(input("Сколько пассажиров посадить? "))
                bus.posadka_person(n)
            elif choice == '2':
                n = int(input("Сколько пассажиров высадить? "))
                bus.visodka_person(n)
            elif choice == '3':
                v = int(input("На сколько увеличить скорость? "))
                bus.speed_up(v)
            elif choice == '4':
                v = int(input("На сколько уменьшить скорость? "))
                bus.speed_down(v)
            elif choice == '5':
                print(f"Текущая скорость: {bus.velocity} км/ч, "
                      f"пассажиров: {bus.persons}, свободных мест: {bus.free_places}")
            elif choice == '6':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Введите корректное число.")
        except SpeedError as e:
            print(f"Ошибка скорости: {e}")
        except PersonError as e:
            print(f"Ошибка количества пассажиров: {e}")

if __name__ == "__main__":
    main()