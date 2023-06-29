"""Провести дисперсионный анализ для определения того,
есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
Даны значения роста в трех группах случайно выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет".
"Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание.
Критерии оценивания: 1 - Слушатель провел дисперсионный анализ для определения того,
есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов."""
import numpy as np
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

x1 = [173, 175, 180, 178, 177, 185, 183, 182]
x2 = [177, 179, 180, 188, 177, 172, 171, 184, 180]
x3 = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]
k = 3
n = 28
x1_mean = np.mean(x1)
x2_mean = np.mean(x2)
x3_mean = np.mean(x3)
total = np.concatenate([x1, x2, x3])
total_mean = np.mean(total)
print(total_mean)
s2_o = np.sum((total - total_mean) ** 2)
print(s2_o)
s2_f = (x1_mean - total_mean) ** 2 * 8 + (x2_mean - total_mean) ** 2 * 9 + (x3_mean - total_mean) ** 2 * 11
print(s2_f)
s2_ost = np.sum((x1 - x1_mean) ** 2) + np.sum((x2 - x2_mean) ** 2) + np.sum((x3 - x3_mean) ** 2)

d_f = s2_f / (k - 1)
print(d_f)
d_ost = s2_ost / (n - k)
print(d_ost)
print(s2_ost)
f_nabl = d_f / d_ost
print(f_nabl)
" f_nabl = 5.5"
f_stats = stats.f_oneway(x1, x2, x3)
print(f_stats)
"""F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698694)"""
"""F табличное для k1 = 2, k2=25 и альфа = 0,05: 3.38; pvalue < альфа принимаем гипотезу H1 " \
"- статистические различия между группами наблюдаются"""

df1 = pd.DataFrame({"score": x1, "group": np.repeat("footbal", repeats=8)})
df2 = pd.DataFrame({"score": x2, "group": np.repeat("hockey", repeats=9)})
df3 = pd.DataFrame(dict(score=x3, group=np.repeat("power lifting", repeats=11)))

df = pd.concat([df1, df2, df3])

tukey = pairwise_tukeyhsd(df["score"], df["group"], alpha=0.05)
print(tukey)
"""F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698694)
     Multiple Comparison of Means - Tukey HSD, FWER=0.05     
=============================================================
 group1     group2    meandiff p-adj   lower    upper  reject
-------------------------------------------------------------
footbal        hockey  -0.4583  0.979  -6.2732  5.3566  False
footbal power lifting  -6.3977 0.0219 -11.9583 -0.8372   True
 hockey power lifting  -5.9394 0.0284 -11.3181 -0.5607   True
-------------------------------------------------------------"""
"""Делаем вывод, что статистически значимые различия в росте есть между группами футболистов и штангистов, 
хоккеистов и штангистов, а между группами хоккеистов и футболистов статистически значимых отличий в росте нет. """



