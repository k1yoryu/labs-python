stroki = int(input("Введите количество строк: "))
stolbci = int(input("Введите количество столбцов: "))

matrix = []
print("Введите элементы матрицы построчно:")
for i in range(stroki):
    row = []
    for j in range(stolbci):
        value = int(input(f"Элемент [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    print(row)
