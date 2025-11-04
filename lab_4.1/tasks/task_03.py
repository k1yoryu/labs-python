import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse, Polygon

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')

ax.set_xticks(range(0, 21, 1))
ax.set_yticks(range(0, 21, 1))
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Рисуем квадрат вручную: левый нижний угол (8, 6), ширина и высота — 4
square = Rectangle((7, 6), 5, 6, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(square)

# Эллипсы — ноги
ear_left = Ellipse((7, 6), width=2.0, height=2.0, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ear_right = Ellipse((12, 6), width=2.0, height=2.0, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(ear_left)
ax.add_patch(ear_right)



# Эллипсы — уши по краям квадрата
ear_left = Ellipse((7, 11.5), width=1.7, height=1.7, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ear_right = Ellipse((12, 11.5), width=1.7, height=1.7, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(ear_left)
ax.add_patch(ear_right)

# Эллипс - голова

head = Ellipse((9.5, 14.8), width=6, height=5.5, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(head)

# Эллипс - нос, треугольник

nos = Ellipse((9.5, 13), width=2, height=2, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(nos)

triangle = Polygon(
    [[8.0, 13.7], [11.0, 13.7], [9.5, 13.0]],  # три точки: левый верх, правый верх, центр
    closed=True,
    facecolor='black',
    edgecolor='black'
)
ax.add_patch(triangle)


plt.show()
