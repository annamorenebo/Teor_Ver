"""Задача 1. Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки
дисперсий для данной выборки."""
import math

import numpy as np

salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]


def average(arr):
    avg = sum((arr[i]) for i in range(0, len(arr))) / len(arr)
    return avg


def disp_dev(arr, avg):
    newarr = np.float_(np.empty_like(salary))
    for i in range(0, len(arr)):
        newarr[i] = (salary[i] - avg) ** 2
        square_dev_with = sum((newarr[i]) for i in range(0, len(arr))) / len(arr)

    return square_dev_with


def disp(arr, avg):
    newarr = np.float_(np.empty_like(salary))
    for i in range(0, len(arr)):
        newarr[i] = (salary[i] - avg) ** 2
        square_dev_without = sum((newarr[i]) for i in range(0, len(arr))) / (len(arr) - 1)

    return square_dev_without


sr_square = math.sqrt(disp(salary, average(salary)))

print(f"Cреднее арифметическое  {average(salary)}")
print(f"Дисперсия без смещения {round(disp(salary, average(salary)), 2)}")
print(f"Дисперсия смещенная {round(disp_dev(salary, average(salary)), 2)}")
print(f'Cреднеквадратичное отклонение  {round(sr_square, 2)}')

"""Cреднее арифметическое  65.3
Дисперсия без смещения 1000.12
Дисперсия смещенная 950.11
Cреднеквадратичное отклонение  31.62"""