"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
 который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print('Автомобиль поехал.')

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")

    def stop(self):
        print("Автомобиль остановился.")

    def turn(self, way):
        print(f"Автомобиль повернул на {way}.")


class TownCar(Car):
    """класс для городских машин"""

    def show_speed(self, maxspeed=60):
        print(f"Текущая скорость: {self.speed} км/ч")
        if self.speed > maxspeed:
            print(f"Вы превысили скорость на {self.speed - maxspeed} км/ч")


class WorkCar(Car):
    """класс для рабочих машин"""

    def show_speed(self, maxspeed=40):
        print(f"Текущая скорость: {self.speed} км/ч")
        if self.speed > maxspeed:
            print(f"Вы превысили скорость на {self.speed - maxspeed} км/ч")


class PoliceCar(Car):
    """класс полицейских машин"""


class SportCar(Car):
    """класс для описания спортивных машин"""


volga = Car()
volga.name = 'Volga'
volga.color = 'white'
volga.is_police = False
volga.speed = 40
print(volga.name, volga.color, volga.speed, volga.is_police)
volga.go()
volga.stop()
volga.turn('юг')
volga.show_speed()

polo = TownCar()
polo.name = 'WV Polo'
polo.color = 'yellow'
polo.speed = 80
polo.is_police = True
print(polo.name, polo.color, polo.speed, polo.is_police)
polo.go()
polo.stop()
polo.turn('восток')
polo.show_speed()

tesla = WorkCar()
tesla.name = 'Tesla'
tesla.color = 'black'
tesla.speed = 100
tesla.is_police = False
print(tesla.name, tesla.color, tesla.speed, tesla.is_police)
tesla.go()
tesla.stop()
tesla.turn('север')
tesla.show_speed()
