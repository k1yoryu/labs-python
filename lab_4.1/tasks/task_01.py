import math
import matplotlib.pyplot as plt

x_grad = [x for x in range(-360, 361)]
x_rad = [math.radians(x) for x in x_grad]

f_x = []
h_x = []

for x in x_rad:
    cos_x = math.cos(x)
    sin_x = math.sin(x)
    cos_06x = math.cos(0.6 * x)

    f = math.exp(cos_x) + math.log(cos_06x ** 2 + 1) * sin_x
    h = -math.log((cos_x + sin_x) ** 2 + 2.5) + 10

    f_x.append(f)
    h_x.append(h)

plt.plot(x_grad, f_x, label='f(x)')
plt.plot(x_grad, h_x, label='h(x)')
plt.title("Графики функций f(x) и h(x)")
plt.xlabel("x (градусы)")
plt.ylabel("Значения функций f(x), h(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
