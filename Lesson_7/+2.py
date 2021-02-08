""" 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (
класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    """ Базовый класс одежды"""

    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    @abstractmethod
    def cover_comsumption(self):
        pass

    @abstractmethod
    def suit_compsumtion(self):
        pass


class Cover(Clothes):
    """Наследованный класс пальто"""

    @property
    def cover_comsumption(self):
        self.textile_amount = int(self.size / 6.5 + 0.5)
        return print(f'Расход ткани для {self.name} составляет {self.textile_amount}м')

    def suit_compsumtion(self):
        pass


class Suit(Clothes):
    """ Наследованный класс костюма"""

    @property
    def suit_compsumtion(self):
        self.textile_amount = int(self.height * 2 + 0.3)
        return print(f'Расход ткани для {self.name} составляет {self.textile_amount}м')

    def cover_comsumption(self):
        pass


my_cover = Cover('Пальто бежевое', 46, 183)
my_cover.cover_comsumption

my_suit = Suit('Костюм женский черный', 46, 1.6)
my_suit.suit_compsumtion
