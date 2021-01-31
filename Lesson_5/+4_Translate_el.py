"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
en_ru = {"One": "Один",
         "Two": "Два",
         "Three": "Три",
         "Four": "Четыре"}
new_list = []
my_file = open("my_file_4.txt", "r", encoding='utf-8')
for line in my_file:  # Превращаем данные из файла в список
    a = line.strip().split()
    new_list.append(a)
print(new_list)
my_file.close()
for i in range(len(new_list)):  # Заменяем 0 значение 1 уровня списка на данные из словаря
    for j in range(len(new_list[i]) - 2):
        new_list[i][0] = en_ru[new_list[i][0]]
print(new_list)







# n_list = [[a for j in range(2)] for i in range(3)]
# new_list.append(a)
# my_file.close()
# print(new_list)
# for i in range(len(new_list)):
#     for j in range(len(new_list[i])-2):
#        new_list[i].insert(0, 5)
# print(new_list)
