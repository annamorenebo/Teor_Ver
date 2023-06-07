"""Задача 5. Устройство состоит из трех деталей.
Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
Какова вероятность того, что в первый месяц выйдут из строя:
а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?"""
p_1 = 0.1
q_1 = 0.9
p_2 = 0.2
q_2 = 0.8
p_3 = 0.25
q_3 = 0.75
p_all = p_1 * p_2 * p_3
p_only2 = p_1 * p_2 * q_3 + p_1 * p_3 * q_2 + q_1 * p_2 * p_3
p_at_least1 = 1 - q_1 * q_2 * q_3
p_from1_to_2 = 1 - q_1 * q_2 * q_3 - p_1 * p_2 * p_3
p_12 = p_1 * p_2 * q_3 + p_1 * p_3 * q_2 + q_1 * p_2 * p_3 + p_1 * q_2 * q_3 + q_1 * p_2 * q_3 + q_1 * q_2 * p_3

print(f"а). все детали - {p_all:.3}  б). только две детали - {p_only2:.3} в)."
      f" хотя бы одна деталь-{p_at_least1:.3} г). от одной до двух деталей -{p_from1_to_2:.3}")

"""а). все детали - 0.005  б). только две детали - 0.08 в). 
хотя бы одна деталь-0.46 г). от одной до двух деталей -0.455"""
