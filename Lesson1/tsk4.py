import math


def details(det, painted, choice):
    m = math.factorial(painted) / (math.factorial(choice) * math.factorial(painted - choice))
    n = math.factorial(det) / (math.factorial(choice) * math.factorial(det - choice))
    p = m / n

    return p


print(f"P= {details(15, 9, 3):.3f}")
"P = 0.185"
