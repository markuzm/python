"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

my_file = open("my_file_7.txt", "r", encoding='utf-8')
content = my_file.readlines()
my_file.close()
print(content)      # Выводим данные из файла
list_for_dict = list()
for el in content:  # Подготавливаем данные для переноса в словарь
    el = (el.strip()).split(' ')
    print(el)
    list_for_dict.append(el)
print(list_for_dict)
my_dict = dict(list_for_dict)    # Превращаем список в словарь
emp_list = []    # Список с фамилиями тех сотрудников, у которых зп менее 20 тыс
print(f"Список фамилий сотрудников с зп менее 20 тыс: {emp_list}")

# summa = 0
# count = 0
# for key, value in my_dict.items():  # Работаем со словарем
#     summa = summa + int(value)
#     count += 1
#     if int(value) < 20000:
#         emp_list.append(key)
#
# print(f"Средняя зп коллектива: {summa/count}")



# data = {
#     "income": {
#         "salary": 50000,
#         "bonus": 20000
#     }
# }
#
# with open("my_file_7.json", "w") as write_f:
#     json.dump(data, write_f)
#
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))
