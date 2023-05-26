
import math


def buttons(quant_buttons, choice):
    n = math.factorial(quant_buttons) / (math.factorial(choice) * math.factorial(quant_buttons - choice))
    m = 1
    p = m/n
    return p


print(f"P= {buttons(10,3):.4f}")
"P = 0,0083"


