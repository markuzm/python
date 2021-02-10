import NumPy


class Matrix:

    def __init__(self, list_el):
        self.list_el = list_el

    def __str__(self):
        return numpy.array(self.list_el)


my_list_1 = Matrix([[1, 2, 3], [3, 4, 5]])
print(f'init: {my_list_1.list_el}')
print(f'str: {my_list_1}')

my_list_2 = Matrix([[6, 7, 8], [9, 10, 11]])
print(f'init: {my_list_2.list_el}')
print(f'str: {my_list_2}')
