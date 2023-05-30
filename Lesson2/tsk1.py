"""1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
Стрелок выстрелил 100 раз.
Найдите вероятность того, что стрелок попадет в цель ровно 85 раз"""
import math


def combin(n, k):
    c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return c


def p_bern(c, n, k, p):
    q = 1 - p
    p = c * math.pow(p, k) * math.pow(q, n - k)
    return p


comb = combin(100, 85)

bern = p_bern(comb, 100, 85, 0.8)
print(f"P={bern:.3f}")

"P=0.048"
