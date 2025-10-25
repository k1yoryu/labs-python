import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
f_x = 5 / (x ** 2 - 9)
plt.plot(x, f_x)
plt.show()