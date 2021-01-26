# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_sum(arg_1, arg_2, arg_3):
    try:
        array = [arg_1, arg_2, arg_3]
        max_1 = max(array)
        array.remove(max_1)
        max_2 = max(array)
        return int(max_1) + int(max_2)
    except ValueError:
        print('Нельзя вводить буквы')

print(my_sum(input('Введите число №1: '), input('Введите число №2: '), input('Введите число №3: ')))