"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
 income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
 (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
 передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Суммарный доход: {self._income}')


worker1 = Position()
worker1.name = 'Леонид'
worker1.surname = 'Великолепный'
worker1._income[wage] = 50000
worker1._income[bonus] = 5000
worker1.get_full_name()
worker1.get_total_income()


