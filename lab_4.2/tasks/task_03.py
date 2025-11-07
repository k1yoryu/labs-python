import numpy as np

A = np.array([
    [-2.0, -8.5, -3.4,  3.5],
    [ 0.0,  2.4,  0.0,  8.2],
    [ 2.5,  1.6,  2.1,  3.0],
    [ 0.3, -0.4, -4.8,  4.6]
])

B = np.array([-1.88,
              -3.28,
              -0.50,
              -2.83])

X = np.linalg.inv(A) @ B

print(f"X = [{', '.join(f'{x:.1f}' for x in X)}]")