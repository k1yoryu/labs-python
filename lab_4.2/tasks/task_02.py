import numpy as np

print("Введите длины участков дороги через пробел:")
lengths = np.array(list(map(float, input().split())))

print("Введите средние скорости на участках через пробел:")
speeds = np.array(list(map(float, input().split())))

print("Введите номер начальноо участка (нумерация с 0):")
k = int(input())

print("Введите номер конечного учатска:")
p = int(input())

segment_lengths = lengths[k:p+1]
segment_speeds = speeds[k:p+1]

S = np.sum(segment_lengths)
times = segment_lengths / segment_speeds
T = np.sum(times)
V = S / T

print(f"S = {S:.2f} км, T = {T:.2f} час, V = {V:.2f} км/ч")