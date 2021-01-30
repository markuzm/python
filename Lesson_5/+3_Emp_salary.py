"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

my_file = open("my_file_3.txt", "r", encoding='utf-8')
content = my_file.readlines()
my_file.close()
print(content)      # Выводим данные из файла
list_for_dict = list()
for el in content:  # Подготавливаем данные для переноса в словарь
    el = (el.strip()).split(' ')
    list_for_dict.append(el)
my_dict = dict(list_for_dict)    # Превращаем список в словарь
emp_list = []    # Список с фамилиями тех сотрудников, у которых зп менее 20 тыс
summa = 0
count = 0
for key, value in my_dict.items():  # Работаем со словарем
    summa = summa + int(value)
    count += 1
    if int(value) < 20000:
        emp_list.append(key)
print(f"Список фамилий сотрудников с зп менее 20 тыс: {emp_list}")
print(f"Средняя зп коллектива: {summa/count}")
