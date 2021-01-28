"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

script, work_hours, hour_price, prize = sys.argv

# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", first_param)
# print("Параметр 2: ", second_param)
# print("Параметр 3: ", third_param)


print(sys.argv)


def motivation_calc(work_hours, hour_price, prize):
    return (work_hours * hour_price) + prize


print(motivation_calc(sys.argv))
