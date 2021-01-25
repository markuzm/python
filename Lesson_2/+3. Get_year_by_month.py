# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_of_the_year = [
    (1, 'winter'),
    (2, 'winter'),
    (12, 'winter'),
    (3, 'spring'),
    (4, 'spring'),
    (5, 'spring'),
    (6, 'summer'),
    (7, 'summer'),
    (8, 'summer'),
    (9, 'autumn'),
    (10, 'autumn'),
    (11, 'autumn')]

try:
    user_month = int(input("Введите номер месяца от 1 до 12: "))
except ValueError:
    print('Вы ввели не число. Введите число от 1 до 12')
except ArithmeticError:
    print('Вы ввели число вне диапазона. Введите число от 1 до 12')
else:
    if (12 <= user_month) or (user_month <= 1):
        print('Вы ввели число вне диапазона. Введите число от 1 до 12')
    else:
        for month, season in month_of_the_year:
            if month == user_month:
                print(season)
                break
