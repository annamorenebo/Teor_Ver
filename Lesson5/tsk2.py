"H0 - шарики имеют диаметр 17 мм"
"H1 -шарики имеют диаметр больше 17 мм"
import math

a = 0.05
n = 100
mu = 17
x_avg = 17.5
disp = 4
sigma = math.sqrt(disp)
z_nabl = (x_avg - mu) / (sigma / math.sqrt(n))
print(z_nabl)
"z_nabl = 2.5"
z_tabl = 1.65
"по таблице"
" z_nabl>z_t значит, гипотеза H0 не верна, принимаем гипотезу H1"
