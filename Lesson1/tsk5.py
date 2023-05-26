import math


def details(bilet, bilet_win, choice):
    m = math.factorial(bilet_win) / (math.factorial(choice) * math.factorial(bilet_win - choice))
    n = math.factorial(bilet) / (math.factorial(choice) * math.factorial(bilet - choice))
    p = m / n

    return p


print(f"P= {details(100, 2, 2):.4f}")
"P = 0.0002"
