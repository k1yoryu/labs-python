user_input = input("Введите строку: ")

result = ""
i = 0

while i < len(user_input):
    count = 1
    while i + 1 < len(user_input) and user_input[i] == user_input[i+1]:
        count += 1
        i += 1
    result += user_input[i] + str(count)
    i += 1
print("Сжатая строка: ", result)