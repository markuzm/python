# 2.Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

before_list = []
a = None


while a != "Стоп":
    a = input("Введите элемент списка. Чтобы прекратить введите 'Стоп':  ")
    before_list.append(a)
before_list.remove("Стоп")


# for a in before_list:
#     a = input("Введите элемент списка. Чтобы прекратить введите 'Стоп':  ")
#     if a == "Стоп":
#         break
#     else:
#         before_list.append(a)

print(f'Список до   : {before_list}')

after_list = []
x = 0
for el in before_list:
    if x % 2 == 0:  # если номер позиции четное число: 0,2,4 и тд
        if x+1 == len(before_list):
            after_list.insert(x, el)
        else:
            next_el = before_list[x+1]
            # print(next_el)
            after_list.insert(x, next_el)
            x += 1
    else:  # если номер позиции нечетное число: 1,3,5 и тд
        prev_el = before_list[x-1]
        # print(prev_el)
        after_list.insert(x, prev_el)
        x += 1
print(f'Список после: {after_list}')