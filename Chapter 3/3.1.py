# step 9
"""Создайте класс Person, у которого есть:

конструктор __init__, принимающий 3 аргумента: name, surname, gender.
 Атрибут gender может принимать только 2 значения: "male" и "female",
 по умолчанию "male". Если в атрибут gender передается любое другое значение,
 печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
 и проставить атрибут gender значением "male"

переопределить метод __str__ следующим образом:
если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>"
если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>"
"""


class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender == 'female' or gender == 'male':
            self.gender = gender
        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f"Гражданин {self.surname} {self.name}"
        elif self.gender == 'female':
            return f"Гражданка {self.surname} {self.name}"


# step 10
"""  Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

конструктор __init__, принимающий произвольное количество аргументов. 
Среди всех переданных аргументов необходимо оставить только целые числа 
и сохранить их в атрибут values в виде списка;
 
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
«Вектор(<value1>, <value2>, <value3>, ...)», если вектор не пустой.
 При этом значения должны быть упорядочены по возрастанию (будьте аккуратнее с пробелами, 
 они стоят только после запятых, см. пример ниже);
 
«Пустой вектор», если наш вектор не хранит в себе значения"""


class Vector:
    def __init__(self, *args):
        self.values = [i for i in args if type(i) == int]

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return 'Пустой вектор'

# step 13
"""Давайте определим магические методы __str__ и __repr__ для класса GroceryItem,
 представляющего продуктовый товар:

Создайте класс GroceryItem, который имеет следующие методы:

метод __init__, который устанавливает значения атрибутов name, price и quantity: 
название товара, его цену и количество
 
магический метод __str__, который возвращает строковое представление товара в следующем виде:
Name: {name}
Price: {price}
Quantity: {quantity}
 

магический метод __repr__, который возвращает однозначное строковое представление объекта
GroceryItem({name}, {price}, {quantity})"""

class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'