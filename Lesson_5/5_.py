"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""
my_file = open("my_file_5.txt", "a")
while True:
    user_answer = input('Введите данные: ')
    if user_answer == " ":
        break
    else:
        my_file.write(user_answer+" ")
my_file.close()
summa = 0
my_file = open("my_file_5.txt", "r")
print('файл', my_file.readlines())
my_list = []
el = my_file.readline()
print('Элемент файла', el)

# for el in my_file:
#
#     print(el.strip())
#     summa = summa + int(el.split().strip())
#     print(summa)
my_file.close()