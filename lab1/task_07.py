seconds = int(input("Секунд: "))
minutes = seconds // 60
new_second = seconds % 60

print(str(minutes) +" мин" + " " + str(new_second) + " сек")
