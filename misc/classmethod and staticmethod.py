# step 7
"""Создайте класс TemperatureConverter, который имеет следующие методы:

 статический метод celsius_to_fahrenheit,
 который принимает температуру в градусах Цельсия и
 переводит ее в градусы по Фаренгейту, используя следующую формулу:


статический метод fahrenheit_to_celsius, который принимает
 температуру в градусах по Фаренгейту и переводит ее в
  градусы по Цельсия, используя следующую формулу:

Во всех этих формулах буква С обозначает градусы по цельсию, а буква F - градусы по Фаренгейту"""


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = celsius * 9 / 5 + 32
        return fahrenheit

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius


# setp 8

""" Перед вами имеется реализация класса RobotVacuumCleaner.
 Сейчас над каждым методом стоит знак _.

Ваша задача сделать код корректным, для это нужно заменить знак
 _ на один из декораторов @staticmethod, @classmethod и @property или же просто удалить знак
. """


class RobotVacuumCleaner:
    name = 'Henry'
    charge = 25

    @classmethod
    def update_charge(cls, new_value):
        cls.charge = new_value

    @staticmethod
    def hello(name):
        return f'Привет, {name}'

    @property
    def data(self):
        return {
            'name': self.name,
            'charge': self.charge
        }

    @classmethod
    def make_clean(self):
        if self.charge < 30:
            return 'Кожаный, заряди меня! Я слаб'
        return 'Я вычищу твою берлогу!!!'


# step 10

""" Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:

класс-метод from_diameter, принимающий диаметр круга.
 Метод from_diameter должен возвращать новый экземпляр класса
  Circle(учитывайте, что экземпляры круга создаются по радиусу);
 
статик-метод is_positive, принимающий одно число. Метод
 is_positive должен возвращать ответ является ли переданное число положительным
 
статик-метод area, который принимает радиус и возвращает площадь круга.
 Для этого воспользуйтесь формулой pi∗r^2 и в качестве значения pi возьмите 3.14
Ваша задача только добавить реализацию трех методов в класс Circle"""


class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return Circle(diameter / 2)

    @staticmethod
    def is_positive(value):
        if value > 0:
            return True
        else:
            return False

    @staticmethod
    def area(radius):
        area = 3.14 * radius ** 2
        return area
