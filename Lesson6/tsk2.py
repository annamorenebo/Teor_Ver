"""Задача 2. В результате 10 независимых измерений некоторой величины X, выполненных с
одинаковой точностью,
получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения
вероятностей,
оценить истинное значение величины X при помощи доверительного интервала,
покрывающего это
значение с доверительной вероятностью 0,95."""
import math

import numpy as np
import scipy.stats as stats

x_array = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
alfa = 0.05
n = 10
x_avg = np.mean(x_array)
D = np.var(x_array, ddof=1)
t = stats.t.ppf(0.975, 9)
print(f"критерий Стьюдента {t:.3}")
delta = t * math.sqrt(D / n)
print(f"Отклонение {delta:.3}")
L = x_avg - delta
U = x_avg + delta
print(f"Доверительный интервал: [{L:.3};{U:.3}]")
"""критерий Стьюдента 2.26
Отклонение 0.322
Доверительный интервал: [6.27;6.91]"""
