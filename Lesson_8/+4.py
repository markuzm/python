"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""

from abc import ABC, abstractmethod


class Business_machines(ABC):
    def __init__(self, name, model, year, serial_number):
        self.name = name
        self.model = model
        self.year = year
        self.serial_number = serial_number

    @abstractmethod
    def start_working(self):
        print('Запуск работы')


class Printer(Business_machines):
    def __init__(self, name, model, year, serial_number, print_type):
        super().__init__(name, model, year, serial_number)
        print_type_value = {'laser', 'jet'}
        if print_type in print_type_value:
            self.print_type = print_type
        else:
            raise ValueError("Не правильный тип данных")

    def start_working(self):
        print(f'Запуск работы принтера')

    def __repr__(self):
        return repr({self.name, self.model, self.year, self.print_type})


class Scaner(Business_machines):
    def __init__(self, name, model, year, serial_number, scan_type):
        super().__init__(name, model, year, serial_number)
        scan_type_value = {'color', 'monochrome'}
        if scan_type in scan_type_value:
            self.scan_type = scan_type
        else:
            raise ValueError("Не правильный тип данных")

    def start_working(self):
        print(f'Запуск работы сканера')

    def __repr__(self):
        return repr({self.name, self.model, self.year, self.scan_type})


class Xerox(Business_machines):
    def __init__(self, name, model, year, serial_number, xerox_type):
        super().__init__(name, model, year, serial_number)
        xerox_type_value = {'one_side_page', 'one_side_page'}
        if xerox_type in xerox_type_value:
            self.xerox_type = xerox_type
        else:
            raise ValueError("Не правильный тип данных")

    def start_working(self):
        print(f'Запуск работы ксерокса')

    def __repr__(self):
        return repr({self.name, self.model, self.year, self.xerox_type})


class Warehouse:
    def __init__(self):
        self.equipment_dict = {}

    def add_to_dict(self, business_machines):
        self.equipment_dict.setdefault(business_machines.serial_number, business_machines)

    def move_eq(self, business_machines, other):
        """перемещение на другой склад"""
        other.add_to_dict(business_machines)
        self.equipment_dict.pop(business_machines.serial_number)


wh1 = Warehouse()
scaner = Scaner('hp', 'x-321', 2015, 's/n: 5', 'color')
wh1.add_to_dict(scaner)
printer = Printer('canon', 'l-456', 2020, 's/n: 7', 'jet')
wh1.add_to_dict(printer)
print(wh1.equipment_dict)
wh2 = Warehouse()
wh1.move_eq(printer, wh2)
print(wh1.equipment_dict)
print(wh2.equipment_dict)
