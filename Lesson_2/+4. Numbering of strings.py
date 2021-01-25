# 4.Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input("Введите любую фразу: ")
new_string = (user_string.split())
print(f"{new_string}")
count = 0
for el in new_string:
    if len(el) > 10:
        print(count, el[:10])
        count += 1
    else:
        print(count, el)
        count += 1
