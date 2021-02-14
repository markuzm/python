"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""


class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


divident = int(input(f"Введите делимое: "))
divider = int(input(f"Введите делитель: "))

try:
    if divider == 0:
        raise DivZero("Деление на ноль недопустимо")
    else:
        print(divident / divider)
except DivZero as dz:
    print(dz)
