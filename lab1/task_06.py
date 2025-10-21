P = float(input("Давление (Па): "))
V = float(input("Объем (м^3): "))
T = float(input("Температура (К): "))

# pV=nRT => n = (pV)/(RT)

R = 8.314
n = (P*V)/(R*T)
print("Количество вещества (моль):", n)
