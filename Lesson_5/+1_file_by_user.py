"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open("my_file_1.txt", "a", encoding='utf-8')
while True:
    user_answer = input('Введите данные: ')
    if user_answer == " ":
        break
    else:
        my_file.write(user_answer+"\n")
my_file.close()
