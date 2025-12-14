# функция, проверяет является ли треугольник прямоугольным
# проверять существует ли треугольник
# Сумма любых двух сторон больше третьей.

def proverka_treygolnika(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    if a + b < c or a + c < b or b + c < a:
        return False
    return a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a