"""Задача 1. Случайная непрерывная величина A имеет равномерное распределение на
промежутке (200, 800].
Найдите ее среднее значение и дисперсию."""
import math

a = 200
b = 800
m = (b - a) / 2
d = (b - a) ** 2 / 12

print(f"среднее значение = {m}, дисперсия = {d} ")
