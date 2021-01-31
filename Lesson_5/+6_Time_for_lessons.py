"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета не обязательно были
все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
new_list = []
my_file = open("my_file_6.txt", "r", encoding='utf-8')
for line in my_file:  # Превращаем данные из файла в список
    a = line.strip().split()
    new_list.append(a)
print(new_list)
my_file.close()

for i in range(len(new_list)):  # Причесывание списка
    for j in range(len(new_list[i])):
        if new_list[i][j].rfind(':') != -1:
            new_list[i][j] = new_list[i][j].rpartition(':')[0]
            continue
        if new_list[i][j].rfind('(') != -1:
            new_list[i][j] = new_list[i][j].rpartition('(')[0]
            continue
        if new_list[i][j].rfind('—') != -1:
            new_list[i][j] = str(0)
            continue
print(new_list)

for i in range(len(new_list)):  # Суммирование элементов и изменение структуры списка для превращения в словарь
    for j in range(len(new_list[i])):
        new_list[i][1] = int(new_list[i][1]) + int(new_list[i][2]) + int(new_list[i][3])
    new_list[i].pop(2)
    new_list[i].pop(2)
print(new_list)

new_dict = dict(new_list)
print(new_dict)
