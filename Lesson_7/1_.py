"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых
математических величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий
шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку
метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д. """


class Iterator:
    """ Объект-итератор """

    def __init__(self, start_i=0, start_j=0):
        self.i = start_i
        self.j = start_j

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 2:
            return self.i
        else:
            raise StopIteration



class Matrix:
    """Объект, поддерживающий интерфейс итерации (итерируемый объект) """

    def __init__(self, list_el):
        self.list_el = list_el

    def __add__(self, other):
        return 10
        # return MyClass(self.width + other.width, self.height + other.height)

    def __str__(self):
        for i in range(len(self.list_el)):
            for j in range(len(self.list_el[i])):
                j += 1
                return f' {self.list_el[i][j]}'
            i += 1
            return '\n'


my_list_1 = Matrix([[1, 2, 3], [3, 4, 5]])
print(f'init: {my_list_1.list_el}')
print(f'str: {my_list_1}')

my_list_2 = Matrix([[6, 7, 8], [9, 10, 11]])
print(f'init: {my_list_2.list_el}')
print(f'str: {my_list_2}')

print(my_list_1 + my_list_2)
