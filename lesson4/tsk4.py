"""Задача 4. Рост взрослого населения города X имеет нормальное распределение,
причем, средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см.
посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
1. больше 182 см?
2. больше 190 см?
3. от 166 см до 190 см?
4. от 166 см до 182 см?
5. от 158 см до 190 см?
6. не выше 150 см или не ниже 190 см?
7. не выше 150 см или не ниже 198 см?
8. ниже 166 см?
Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.),
 а затем проверить себя с помощью встроенных функций"""
import numpy as np
import scipy.stats

m_x = 174
s = 8
z_1 = 68
z_2 = 95.4
z_3 = 99.72


def p_x(height, m_x, s):
    z = (height - m_x) / s
    if z == 1 or z == -1:
        p = (100 - z_1) / 2
    elif z == 2 or z == -2:
        p = (100 - z_2) / 2
    elif z == 3 or z == -3:
        p = (100 - z_3) / 2

    return p


def numpy_use(m_x, s, height):
    scipy.stats.norm(loc=m_x, scale=s).cdf(height)

print("Значения без спец. функций:")
print(f"P(x>182) = {p_x(182, m_x, s)} %")
print(f"P(x>190) = {p_x(190, m_x, s):.2} %")
print(f"P(166>x<190) = {100 - p_x(166, m_x, s) - p_x(190, m_x, s)} %")
print(f"P(166>x<182) = {100 - p_x(166, m_x, s) - p_x(182, m_x, s)} %")
print(f"P(158>x<190) = {100 - p_x(158, m_x, s) - p_x(190, m_x, s)} %")
print(f"P(x<150 +x>190) = {(p_x(150, m_x, s) + p_x(190, m_x, s)):.3} %")
print(f"P(x<150 +x>198) = {(p_x(150, m_x, s) + p_x(198, m_x, s)):.3} %")
print(f"P(x<160) = {p_x(166, m_x, s):.3} %")
print("Значения со  спец. функциями:")
print(f"P(x>182) = {round(((1 - scipy.stats.norm(loc=174, scale=8).cdf(182)) * 100), 0)}%")
print(f"P(x>190) = {((1 - scipy.stats.norm(loc=174, scale=8).cdf(190)) * 100):.2}%")
print(f"P(166>x<190) = {(scipy.stats.norm(loc=174, scale=8).cdf(190) - scipy.stats.norm(loc=174, scale=8).cdf(166))*100:.3} % ")
print(f"P(166>x<182) = {(scipy.stats.norm(loc=174, scale=8).cdf(182) - scipy.stats.norm(loc=174, scale=8).cdf(166))*100:.3} % ")
print(f"P(158>x<190) = {(scipy.stats.norm(loc=174, scale=8).cdf(190) - scipy.stats.norm(loc=174, scale=8).cdf(158))*100:.3} % ")
print(f"P(x<158+x>190) = {((1-scipy.stats.norm(loc=174, scale=8).cdf(190)) + scipy.stats.norm(loc=174, scale=8).cdf(150))*100:.3} % ")
print(f"P(x<158+x>198) = {((1-scipy.stats.norm(loc=174, scale=8).cdf(198)) + scipy.stats.norm(loc=174, scale=8).cdf(150))*100:.3} % ")
print(f"P(x<166) = {(scipy.stats.norm(loc=174, scale=8).cdf(166))*100:.3} % ")
"""
Значения без спец. функций:
P(x>182) = 16.0 %
P(x>190) = 2.3 %
P(166>x<190) = 81.7 %
P(166>x<182) = 68.0 %
P(158>x<190) = 95.4 %
P(x<150 +x>190) = 2.44 %
P(x<150 +x>198) = 0.28 %
P(x<160) = 16.0 %
Значения со  спец. функциями:
P(x>182) = 16.0%
P(x>190) = 2.3%
P(166>x<190) = 81.9 % 
P(166>x<182) = 68.3 % 
P(158>x<190) = 95.4 % 
P(x<158+x>190) = 2.41 % 
P(x<158+x>198) = 0.27 % 
P(x<166) = 15.9 % """