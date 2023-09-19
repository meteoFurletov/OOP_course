# step 2
"""Создайте класс Rectangle, у которого есть:

конструктор __init__, принимающий 2 аргумента: длину и ширину.
свойство area, которое возвращает площадь прямоугольника;"""

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width

# step 3

"""  Создайте класс Date, у которого есть:

конструктор __init__, принимающий 3 аргумента: день, месяц и год. 
 
свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
 
свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";
"""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:04}'

# step 4
"""Создайте класс Password, который имеет:

метод __init__, который устанавливает значение атрибута password
 
вычисляемое свойство strength, которое определяет стойкость пароля. 
Если длина пароля меньше 8 символов, то такой пароль считается слабым, 
свойство должно вернуть строку  "Weak". Сильным паролем считается тот,
 в котором длина символов 12 и более, в таком случае свойство возвращает строку 
 "Strong". Во всех остальных случаях необходимо вернуть "Medium"""

class Password:
    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        if len(self.password) < 8:
            return 'Weak'
        elif len(self.password) >= 12:
            return 'Strong'
        else:
            return 'Medium'
