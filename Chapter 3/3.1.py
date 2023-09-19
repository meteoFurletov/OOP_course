# step 9

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

class Vector:
    def __init__(self, *args):
        self.values = [i for i in args if type(i) == int]

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return 'Пустой вектор'


# step 13

class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'
