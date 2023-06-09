"""Задача 2. О случайной непрерывной равномерно распределенной величине B известно, что ее
дисперсия равна 0.2.
Можно ли найти правую границу величины B и ее среднее значение зная, что левая
граница равна 0.5?
Если да, найдите ее."""
import math

a = 0.5
d = 0.2

b = a + math.sqrt(d * 12)
m = (b - a) / 2
print(f"правая граница равна {b:.3}, среднее значение равно {m:.2}")

"правая граница равна 2.05, среднее значение равно 0.77"
