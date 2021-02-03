"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
 Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
 Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
 толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    # атрибуты класса

    # length = 5
    # width = 25

    # def __init__(self, length, width):
    #     self.length = length
    #     self.width = width

    # def __str__(self):
    #     return f'{self.length} ({self.width})'

    def asphalp_mass_calc(self, length, width, h = 5, kg = 25):
        self.mass = length * width * h * kg
        return f'{self.mass}'

road1 = Road()
print(road1)
print(type(road1))
print(road1.asphalp_mass_calc(20, 5000))

# road1 = road(2,5)
# a = road1.asphalp_mass_calc(20, 5000)
# print(road1)
# print(a)

