"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open("my_file_2.txt", "r", encoding='utf-8')
content = my_file.readlines()
print(content)   # Загруженный из файла список
print(f'Кол-во строк: {str(len(content))}')
i = 0
for el in content:
    words = el.split(' ')
    print(words)    # Список слов, входящих в i строчку
    print(f'Кол-во слов в {i+1} строке: {str(len(words))}')
    i += 1
my_file.close()
