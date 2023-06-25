"""Задача 1 Даны значения величины заработной платы заемщиков банка (zp) и значения их
поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические
операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату
(то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая
переменная). Произвести расчет как с использованием intercept, так и без."""
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import LinearRegression

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(zp)
"""нахождение коэффициентов математическим способом:"""
b1 = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp ** 2) - (np.mean(zp)) ** 2)
print(f"b1 = {b1:.4}")
b0 = np.mean(ks) - b1 * np.mean(zp)
print(f"b0 = {b0:.4}")
print(f"математическая модель: ks = {b0:.4} + {b1:.4}*zp")

ks_pred = np.array(b0 + b1 * zp)
r = np.corrcoef(zp, ks)[1, 0]
print(f"R^2 = {round(r ** 2,2)}")
mse = np.sum((ks - ks_pred) ** 2) / n
print(f"mse = {mse:.6}")
"критерий Фишера"
f_nabl = (r ** 2) / ((1 - r ** 2) / 8)
f = stats.f.ppf(0.975, 1, 8)
print(f"f_nabl = {f_nabl:.3} >f_krit={f:.3} отвергаем гипотезу о не значимости модели")

print("нахождение значений коэффициента b1 матричным способом без константы:")
zp = zp.reshape(1, n)
ks = ks.reshape(1, n)
b1_1 = np.dot(np.dot(np.linalg.inv(np.dot(zp, zp.T)), zp), ks.T)
print(f"коэффициент b1  без  константы: {b1_1[0,0]:.3}")
ks_pred_1 = b1_1 * zp
mse1 = mse = np.sum((ks - ks_pred_1) ** 2) / n
print(f"mse = {mse1:.6}")

print("нахождение значений коэффициентов матричным способом с константой:")
zp_1 = np.vstack([np.ones((1, 10)), zp])
coef = np.dot(np.dot(np.linalg.inv(np.dot(zp_1, zp_1.T)), zp_1), ks.T)
print(f"b0 = {round(coef[0, 0],2)}, b1 = {round(coef[1, 0],2)} ")

print("нахождение значений коэффициентов c помощью функции intercept:")

model = LinearRegression()
zp = zp.reshape(-1, 1)
ks = ks.reshape(-1, 1)
model.fit(zp, ks)
r_2 = model.score(zp, ks)
print(f"R^2 = {r_2:.3}")
print(f"константа b0 = {model.intercept_[0]:.5}")
print(f" b1 = {model.coef_[0,0]:.3}")

"""
b1 = 2.621
b0 = 444.2
математическая модель: ks = 444.2 + 2.621*zp
R^2 = 0.79
mse = 6470.41
f_nabl = 29.7 >f_krit=7.57 отвергаем гипотезу о не значимости модели
нахождение значений коэффициента b1 матричным способом без константы:
коэффициент b1  без  константы: 5.89
mse = 56516.9
нахождение значений коэффициентов матричным способом с константой:
b0 = 444.18, b1 = 2.62 
нахождение значений коэффициентов c помощью функции intercept:
R^2 = 0.788
константа b0 = 444.18
 b1 = 2.62"""

