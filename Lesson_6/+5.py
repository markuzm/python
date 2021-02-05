"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
 и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
  (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
   Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
    что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title = ''

    def draw(self):
        return "Запуск отрисовки"

class Pen(Stationery):
    def draw(self):
        print(f'{(super().draw())} {str(self.title)[:4]}и')

class Handle(Stationery):
    def draw(self):
        print(f'{(super().draw())} {self.title}a')

class Pensil(Stationery):
    def draw(self):
        print(f'{(super().draw())} {self.title}a')

my_pen = Pen()
my_pen.title = 'ручка'
my_pen.draw()

my_handle = Handle()
my_handle.title = "маркер"
my_handle.draw()

my_pensil = Pensil()
my_pensil.title = "карандаш"
my_pensil.draw()


