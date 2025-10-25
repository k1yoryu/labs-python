import matplotlib.pyplot as plt
import numpy as np

x_grad = np.linspace(-360, 360, 1000)
x_rad = np.radians(x_grad)

f_x = np.exp(np.cos(x_rad)) + np.log(np.cos(0,6 * x_rad) ** 2 + 1) * np.sin(x_rad)
h_x = -np.log((np.cos(x_rad) + np.sin(x_rad)) ** 2 + 2.5) + 10
plt.plot(x_grad, f_x)
plt.plot(x_grad, h_x)
plt.show()