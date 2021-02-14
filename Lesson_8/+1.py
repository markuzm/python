"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:

    @classmethod
    def date_to_int(cls, date):
         day, month, year = map(int, date.split('-'))
         return print(day, month, year)

    @staticmethod
    def time_validation(day, month, year):
        if 1 <= day <= 31:
            pass
        else:
            print(f'Вы ввели {day}. Дата должна быть в пределах от 1 до 31')
        if 1 <= month <= 12:
            pass
        else:
            print(f'Вы ввели {month}. Месяц должен быть в пределах от 1 до 12')
        if year > 1900:
            pass
        else:
            print(f'Вы ввели {year}. Год должен быть больше 0 ')


my_date_1 = Date.date_to_int('2-2-2022')
Date.time_validation(12, 13, 2015)
