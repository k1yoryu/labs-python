def transpose_matrix(matrix):

    stroki = len(matrix)
    stolbci = len(matrix[0])

    transposed = []
    for j in range(stolbci):
        new_row = []
        for i in range(stroki):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed

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

transposed = transpose_matrix(matrix)

print("\nТранспонированная матрица:")
for row in transposed:
    print(row)
