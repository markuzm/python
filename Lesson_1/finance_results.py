# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

revenue: int = int(input("Введите значение выручки:"))
cost = int(input("Введите значение убытков:"))
profit = 0
loss = 0
if revenue < cost:
    loss = cost - revenue
    print("Доходы:", revenue, "\nЗатраты:", cost, "\nУбыток:", loss)
elif revenue > cost:
    profit = revenue - cost
    profit_margin = round(profit / revenue, 2) * 100
    print(f"Доходы: {revenue} \nЗатраты: {cost} \nВыручка: {profit} \nУбыток: {loss} "
          f"\nРентабельность,%: {profit_margin}")
    count_employees = int(input("Введите количество сотрудников:"))
    profit_per_employee = round(profit / count_employees, 2)
    print(f"Численность персонала: {count_employees} \nДоход на сотрудника: {profit_per_employee}")
else:
    print("Доходы равны затратам")
