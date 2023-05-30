"""3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?"""
import math


def combin(n, k):
    c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return c


def p_bern(c, n, k, p):
    q = 1 - p
    p = c * math.pow(p, k) * math.pow(q, n - k)
    return p


comb = combin(144, 70)

bern = p_bern(comb, 144, 70, 0.5)
print(f"P={bern:.3f}")
"P=0.063"
