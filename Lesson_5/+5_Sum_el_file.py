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
        my_file.write(user_answer + " ")
my_file.close()

my_file = open("my_file_5.txt", "r")
# print("Элементы файла:", my_file.readlines())  - если файл открыт на чтение, то нельзя его последовательно
# считывать сначала полностью (readlines), а потом построчно (readline)?
my_list = my_file.readline().split()
summa = 0
for el in my_list:
    summa += int(el)
print("Сумма всех элементов файла:", summa)
my_file.close()

# Из методички
# my_f = open("my_file_5.txt", "r")
# content = my_f.readlines()
# el = my_f.readline()
# print(content, el)
# my_f.close()
