import numpy as np
from scipy import integrate

#Определенный интеграл
print("Интеграл: ∫ [sin(x) + x*cos(x) + x^2 + e^{-x}]dx")

print("""\nСводка:
π     ≈ 3.1416
2π    ≈ 6.2832
π/2   ≈ 1.5708
π/3   ≈ 1.0472
2π/3  ≈ 2.0944
π/4   ≈ 0.7854
3π/2  ≈ 4.7124\n""")

a = float(input("Нижний предел (a): "))
b = float(input("Верхний предел (b): "))

f1 = lambda x: np.sin(x) + x * np.cos(x) + x**2 + np.exp(-x)
result1, _ = integrate.quad(f1, a, b)

print(f"\nОдномерный интеграл: {result1:.6f}\n")

#Двойной интеграл
print("Интеграл: ∬ [ sin(x^2) * cos(y) + e^(-x*y) + ln(1 + x^2 + y^2) ] dx dy")

print("""\nСводка:
π     ≈ 3.1416
2π    ≈ 6.2832
π/2   ≈ 1.5708
π/3   ≈ 1.0472
2π/3  ≈ 2.0944
π/4   ≈ 0.7854
3π/2  ≈ 4.7124\n""")

x_a = float(input("Пределы по x от: "))
x_b = float(input("Пределы по x до: "))
y_c = float(input("Пределы по y от: "))
y_d = float(input("Пределы по y до: "))

f_2 = lambda y, x: np.sin(x**2) * np.cos(y) + np.exp(-x * y) + np.log(1 + x**2 + y**2)

result, _ = integrate.dblquad(f_2, x_a, x_b, y_c, y_d)

print(f"\nДвойной интеграл: {result:.6f}")