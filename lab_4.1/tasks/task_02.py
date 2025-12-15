import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 5 / (x**2 - 9)

x1 = np.linspace(-10, -3.01, 500)
x2 = np.linspace(-2.99, 2.99, 500)
x3 = np.linspace(3.01, 10, 500)

plt.plot(x1, f(x1))
plt.plot(x2, f(x2))
plt.plot(x3, f(x3))

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axvline(x=3, color='red', linestyle='--', linewidth=0.5)
plt.axvline(x=-3, color='red', linestyle='--', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title(r"График функции $f(x) = \frac{5}{x^2 - 9}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()