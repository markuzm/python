"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых
математических величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий
шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку
метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д. """


class Matrix:

    def __init__(self, list_el):
        self.list_el = list_el

    def __str__(self):
        answer = ''
        for i in range(len(self.list_el)):
            answer += '\n'
            for j in range(len(self.list_el[i])):
                answer = answer + str(self.list_el[i][j]) + " "
                j += 1
            i += 1
        return answer

    def __add__(self, other):
        new_matrix = []
        new_matrix_line = []
        summa = 0
        for i in range(len(self.list_el)):
            for j in range(len(self.list_el[0])):
                summa = other.list_el[i][j] + self.list_el[i][j]
                new_matrix_line.append(summa)
                if len(new_matrix_line) == len(self.list_el[0]):
                    new_matrix.append(new_matrix_line)
                    new_matrix_line = []
        return Matrix(new_matrix)


my_list_1 = Matrix([[1, 2, 3], [3, 4, 5]])
print(f'init: {my_list_1.list_el}')
print(f'str: {my_list_1.__str__()}')

my_list_2 = Matrix([[6, 7, 8], [9, 10, 11]])
print(f'init: {my_list_2.list_el}')
print(f'str: {my_list_2.__str__()}')

print(my_list_1 + my_list_2)
