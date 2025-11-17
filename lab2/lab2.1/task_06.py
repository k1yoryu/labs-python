user_input = input("Введите элементы через пробел: ")
parts = user_input.split()

unique = []
for element in parts:
    if element not in unique:
        unique.append(element)
print("Список без дубликатов: ", unique)