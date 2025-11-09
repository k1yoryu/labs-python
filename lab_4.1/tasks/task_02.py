import matplotlib.pyplot as plt

def f(x):
    return 5 / (x**2 - 9)

all_segments = []

x = -10.0
xs, ys = [], []
while x < -3.0:
    xs.append(x)
    ys.append(f(x))
    x += 0.05
all_segments.append((xs, ys))

x = -2.99
xs, ys = [], []
while x < 3.0:
    xs.append(x)
    ys.append(f(x))
    x += 0.05
all_segments.append((xs, ys))

x = 3.01
xs, ys = [], []
while x <= 10.0:
    xs.append(x)
    ys.append(f(x))
    x += 0.05
all_segments.append((xs, ys))

for xs, ys in all_segments:
    plt.plot(xs, ys, 'b-')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title(r"График функции $f(x) = \frac{5}{x^2 - 9}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axvline(x=3, color='red', linestyle='--', linewidth=0.5)
plt.axvline(x=-3, color='red', linestyle='--', linewidth=0.5)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()