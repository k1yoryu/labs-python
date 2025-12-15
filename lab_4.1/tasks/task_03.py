import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse, Polygon
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')

ax.set_xticks(range(0, 21, 1))
ax.set_yticks(range(0, 21, 1))
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

#квадрат - туловище
# square = Rectangle((7, 6), 5, 6, facecolor='saddlebrown', edgecolor='black', linewidth=2)
# ax.add_patch(square)

tuloviche = Ellipse((9.5, 9), width=5.0, height=6.0, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(tuloviche)

# Эллипсы — ноги
ear_left = Ellipse((7, 6), width=2.0, height=2.0, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ear_right = Ellipse((12, 6), width=2.0, height=2.0, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(ear_left)
ax.add_patch(ear_right)

noga_vnutri_r =  Ellipse((7, 6), width=1.2, height=1.2, facecolor='pink', linewidth=2)
noga_vnutri_l =  Ellipse((12, 6), width=1.2, height=1.2, facecolor='pink', linewidth=2)
ax.add_patch(noga_vnutri_r)
ax.add_patch(noga_vnutri_l)


# Эллипсы — руки по краям квадрата
ear_left = Ellipse((7, 11.5), width=1.7, height=1.7, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ear_right = Ellipse((12, 11.5), width=1.7, height=1.7, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(ear_left)
ax.add_patch(ear_right)
lapa_vnutri_r = Ellipse((7, 11.5), width=0.9, height=0.9, facecolor='pink', linewidth=2)
ax.add_patch(lapa_vnutri_r)
lapa_vnutri_l = Ellipse((12, 11.5), width=0.9, height=0.9, facecolor='pink', linewidth=2)
ax.add_patch(lapa_vnutri_l)

# левая ухо (внешняя часть)
ear_left = Ellipse((7.5, 16.7), width=1.6, height=1.6, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(ear_left)

# левая ухо (внутренняя часть)
inner_ear_left = Ellipse((7.5, 16.7), width=0.9, height=0.9, facecolor='peru', edgecolor='none')
ax.add_patch(inner_ear_left)

# правое ухо (внешняя часть)
ear_right = Ellipse((11.5, 16.7), width=1.6, height=1.6, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(ear_right)

# правое ухо (внутренняя часть)
inner_ear_right = Ellipse((11.5, 16.7), width=0.9, height=0.9, facecolor='peru', edgecolor='none')
ax.add_patch(inner_ear_right)


# Эллипс - голова
head = Ellipse((9.5, 14.8), width=6, height=5.5, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(head)

# Эллипс - нос, треугольник
nos = Ellipse((9.5, 13), width=2, height=2, facecolor='saddlebrown', edgecolor='black', linewidth=2)
ax.add_patch(nos)

triangle = Polygon(
    [[9.0, 13.7], [10.0, 13.7], [9.5, 13.0]],  # три точки: левый верх, правый верх, центр
    closed=True,
    facecolor='black',
    edgecolor='black'
)
ax.add_patch(triangle)

#Левый глаз
eye_white1 = Ellipse((8, 15), width=1.3, height=1.3, facecolor='white', edgecolor='black', linewidth=2)
ax.add_patch(eye_white1)

iris1 = Ellipse((8, 15), width=0.7, height=0.7, facecolor='saddlebrown', edgecolor='black', linewidth=1)
ax.add_patch(iris1)

pupil1 = Ellipse((8, 15), width=0.3, height=0.3, facecolor='black', edgecolor='black')
ax.add_patch(pupil1)

highlight1 = Ellipse((8.1, 15.1), width=0.12, height=0.12, facecolor='white', edgecolor='none')
ax.add_patch(highlight1)

#Правый глаз
eye_white2 = Ellipse((11, 15), width=1.3, height=1.3, facecolor='white', edgecolor='black', linewidth=2)
ax.add_patch(eye_white2)

iris2 = Ellipse((11, 15), width=0.7, height=0.7, facecolor='saddlebrown', edgecolor='black', linewidth=1)
ax.add_patch(iris2)

pupil2 = Ellipse((11, 15), width=0.3, height=0.3, facecolor='black', edgecolor='black')
ax.add_patch(pupil2)

highlight2 = Ellipse((11.1, 15.1), width=0.12, height=0.12, facecolor='white', edgecolor='none')
ax.add_patch(highlight2)
# ax.axis('off')


# # 9.5 12.5
# square = Rectangle((9.5, 12), 1, 2, facecolor='red', edgecolor='black', linewidth=2)
# ax.add_patch(square)

# plt.plot([9.2,9.8],[12.6,12.6], color="red", linewidth=6)
# rot_el = Ellipse((9.5, 12.5), width=0.5, height=0.5, facecolor='red', edgecolor='none')
# ax.add_patch(rot_el)

theta = np.linspace(0, np.pi, 100)
x = 9.8 + 0.3 * np.cos(theta)
y = 13.0 - 0.6 * np.sin(theta)
plt.plot(x, y, color="black", linewidth=2)

theta = np.linspace(0, np.pi, 100)
x = 9.1 - 0.3 * np.cos(theta)
y = 13.0 - 0.6 * np.sin(theta)
plt.plot(x, y, color="black", linewidth=2)

# УСЫ
plt.plot([7, 9], [14, 13], color="black", linewidth=1)
plt.plot([7, 9], [13, 13], color="black", linewidth=1)
plt.plot([7, 9], [12, 13], color="black", linewidth=1)

plt.plot([10, 12], [13, 14], color="black", linewidth=1)
plt.plot([10, 12], [13, 13], color="black", linewidth=1)
plt.plot([10, 12], [13, 12], color="black", linewidth=1)
plt.show()