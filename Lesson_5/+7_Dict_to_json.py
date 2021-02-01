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
print(content)  # Выводим данные из файла
list_for_dict = list()

for el in content:  # Подготавливаем данные для переноса в словарь
    el = (el.strip()).split(' ')
    list_for_dict.append(el)
print(list_for_dict)

summa = 0
count = 0
for i in range(len(list_for_dict)):  # Превращаем список в словарь
    for j in range(len(list_for_dict[i])):
        my_dict = {list_for_dict[i][0]: int(list_for_dict[i][2]) - int(list_for_dict[i][3]) for i in range(5)}
    count += 1
    summa += (int(list_for_dict[i][2]) - int(list_for_dict[i][3]))
print('Словарь:', my_dict)

my_list = [my_dict, {'average_profit': int(summa / count)}]  # Создаем список из словарей
print(my_list)

with open("my_file_7.json", "w") as write_f:  # Выгружаем список в json
    json.dump(my_list, write_f)
