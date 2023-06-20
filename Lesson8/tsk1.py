"""Задача 1 Даны значения величины заработной платы заемщиков банка (zp) и значения их
поведенческого кредитного скоринга (ks):
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с
помощью функции cov из numpy
Полученные значения должны быть равны.
Найдите коэффициент корреляции Пирсона с помощью ковариации и
среднеквадратичных отклонений двух признаков,
а затем с использованием функций из библиотек numpy и pandas."""
import numpy as np
import pandas as pd

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov1 = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
print(f"ковариация  с помощью элементарных действий:{cov1:.6}")
print(f"c помощью функции cov из numpy {np.cov(zp, ks, ddof=0)}")

std_zp = np.std(zp, ddof=0)
std_ks = np.std(ks, ddof=0)

pirs1 = 9157.84 / (std_zp * std_ks)
print(f"коэффициент корреляции Пирсона с помощью ковариации исреднеквадратичных отклонений двух признаков: {pirs1:.3}")

print(f"с использованием функций из библиотек numpy {np.corrcoef(zp, ks)}")


df = pd.DataFrame({'zp': zp, 'ks': ks})

pdcorr = df['zp'].corr(df['ks'])
print(f'4. Расчет коэффициента корреляции в pandas: {pdcorr:.3}')
"""ковариация  с помощью элементарных действий:9157.84
c помощью функции cov из numpy [[ 3494.64  9157.84]
 [ 9157.84 30468.89]]
коэффициент корреляции Пирсона с помощью ковариации исреднеквадратичных отклонений двух признаков: 0.887
с использованием функций из библиотек numpy [[1.         0.88749009]
 [0.88749009 1.        ]]
4. Расчет коэффициента корреляции в pandas: 0.887
Сильная линейная корреляция"""
