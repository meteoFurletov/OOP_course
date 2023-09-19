# step 11
"""Создайте класс  Fruit, который имеет:

метод __init__, который устанавливает значения атрибутов name и price: название и цена фрукта

методы сравнения. Здесь вы сами решаете какие магические методы реализовывать,
 главное чтобы фрукты могли сравниваться с числами и другими фруктами по цене.
 Смотрите тесты ниже в коде"""

from functools import total_ordering


@total_ordering
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price == other

    def __lt__(self, other):
        if isinstance(other, Fruit):
            return self.price < other.price
        elif isinstance(other, (int, float)):
            return self.price < other

    def __le__(self, other):
        if isinstance(other, Fruit):
            return self.price < other.price or self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price < other or self.price == other


# step 12
"""Для выражения относительной силы шахматистов используется система рейтингов.
 Наиболее популярная система рейтингов, которая используется Международной
  шахматной федерацией (ФИДЕ), большинством других шахматных федераций и игровых шахматных сайтов,
   является система рейтингов Эло.

В зависимости от выступлений на различных соревнованиях каждому шахматисту начисляются 
баллы в его рейтинг. Давайте с вами реализуем класс ChessPlayer и научимся сравнивать 
рейтинги шахматистов между собой.

И так, ваша задача реализовать класс ChessPlayer, который состоит из:

метода инициализации, принимающего аргументы name, surname, rating;
 
магического  метода __eq__, который будет позволять сравнивать экземпляры класса 
ChessPlayer с числами и другими экземплярами этого класса. Если сравнение происходит с 
целым числом и атрибут rating с ним совпадает, то необходимо вернуть True, в противном случае
 - False. Если же сравнение идет с другим шахматистом(экземпляром класса ChessPlayer)  и 
 значения атрибутов rating равны, то возвращается True, в противном случае - False. А 
 если же сравнивается с другим типом данных, верните ‘Невозможно выполнить сравнение’;
 
магического  метода __gt__. Если сравнение происходит с целым числом и атрибут rating больше 
его, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит 
с другим шахматистом(экземпляром класса ChessPlayer) и атрибут rating у нашего экземпляра больше,
 то верните True, в противном случае - False. В случае если сравнение идет с остальными типами 
 данных, верните ‘Невозможно выполнить сравнение’
 
магического  метода __lt__. Если сравнение происходит с целым числом и атрибут rating меньше 
его, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит 
с другим шахматистом(экземпляром класса ChessPlayer) и атрибут rating у нашего экземпляра меньше, 
то верните True, в противном случае - False. В случае если сравнение идет с остальными типами
 данных, верните ‘Невозможно выполнить сравнение’."""


class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        elif isinstance(other, (int, float)):
            return self.rating == other
        else:
            return "Невозможно выполнить сравнение"

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        elif isinstance(other, (int, float)):
            return self.rating > other
        else:
            return "Невозможно выполнить сравнение"

    def __lt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        elif isinstance(other, (int, float)):
            return self.rating < other
        else:
            return "Невозможно выполнить сравнение"


# step 14
"""Создайте класс  Rectangle, который имеет:

метод __init__, который устанавливает значения атрибутов width и height:
 ширина и высота прямоугольника
 
свойство area, возвращающее площадь прямоугольника
 
методы сравнения. Здесь вы сами решаете какие магические методы реализовывать,
 главное чтобы прямоугольники могли сравниваться с числами и между собой по значению площади.
  Используйте декоратор  @total_ordering"""


@total_ordering
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        elif isinstance(other, (int, float)):
            return self.area == other

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area <= other.area
        elif isinstance(other, (int, float)):
            return self.area <= other
