
import math


def cards(quant_card, mast_quant, choice):
    m = math.factorial(mast_quant) / (math.factorial(choice) * math.factorial(mast_quant - choice))
    n = math.factorial(quant_card) / (math.factorial(choice) * math.factorial(quant_card - choice))
    return m / n


print(f"P= {cards(52, 13, 4):.4f}")
"P = 0,0026"


