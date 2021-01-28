"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
multiple = 1
for el in [el for el in range(100, 1001) if el % 2 == 0]:
    multiple = multiple * el
print("Произведение всех элементов:", multiple)


# Менее компактная реализация
# multiple = 1
# new_script = [el for el in range(100, 1001) if el % 2 == 0]
# print(new_script)
# for el in new_script:
#     multiple = multiple * el
# print(multiple)
# print(len(str(multiple)))
# print(len(new_script))

