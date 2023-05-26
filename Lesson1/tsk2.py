import math


def cards(quant_card, quant_without_aces, choice):
    m = math.factorial(quant_without_aces) / (math.factorial(choice) * math.factorial(quant_without_aces - choice))
    n = math.factorial(quant_card) / (math.factorial(choice) * math.factorial(quant_card - choice))
    p = 1 - m / n
    return p


print(f"P= {cards(52, 48, 4):.2f}")
"P = 0.28"
