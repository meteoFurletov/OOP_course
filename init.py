# step 2.1.8

class Lion:
    def roar(self):
        print('Rrrrrrr!!!')


# step 2.1.9

class Robot:
    def say_hello(self):
        print('Hello, human! My name is C-3PO')

    def say_bye(self):
        print('See u later alligator')


# step 2.1.10

class Robot:
    def set_name(self, name):
        setattr(self, 'name', name)

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')


# step 2.1.11

class Counter:
    def start_from(self, value=0):
        setattr(self, 'value', value)

    def increment(self):
        self.value += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.value}')

    def reset(self):
        self.value = 0


# step 2.1.12

class Constructor:
    def add_attribute(self, name, value):
        setattr(self, name, value)

    def display(self):
        print(self.__dict__)


# step 2.1.13
class Point:
    def set_coordinates(self, x, y):
        setattr(self, 'x', x)
        setattr(self, 'y', y)

    def get_distance(self, second_point):
        if isinstance(second_point, Point):
            return ((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2) ** (0.5)
        else:
            print('Передана не точка')


# step 2.2.9
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = self.brand + " " + self.model


laptop1 = Laptop("whatever", "whatever", 1)
laptop2 = Laptop("whatever", "whatever", 2)


# step 2.211

class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goal=1):
        self.goals += goal

    def make_assist(self, assist=1):
        self.assists += assist

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


# step 2.2.12

class Zebra:
    def __init__(self, color=0):
        self.color = color

    def which_stripe(self):
        if self.color == 0:
            print("Полоска белая")
            self.color = 1
        elif self.color == 1:
            print("Полоска черная")
            self.color = 0


# step 2.2.13

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


# step 2.3.2

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f'{self.name} says {sound}'


# step 2.3.3

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


# step 2.3.4

class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.is_empty():
            print('Empty Stack')
        else:
            return self.values.pop()

    def peek(self):
        if self.is_empty():
            print('Empty Stack')
            return None
        return self.values[-1]

    def size(self):
        return len(self.values)


# step 2.3.6

class Worker:

    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f"Worker {self.name}; passport-{self.passport}")


persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')]

worker_objects = []

for elem in persons:
    worker_objects.append(Worker(*elem))

for elem in worker_objects:
    elem.get_info()


# step 2.3.7

class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def config(self, **kwargs):
        self.__dict__.update(**kwargs)


# step 2.3.8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee:
    def __init__(self, name, age, company_name, company_location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, company_location)


# step 2.3.11

class Task:
    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        print(f"{self.name} {'(Сделана)' if self.status == True else '(Не сделана)'}")


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager:
    def __init__(self, task_list):
        self.task_list = task_list

    def change_status(self, task, status):
        task.status = status

    def mark_done(self, task):
        self.change_status(task, True)

    def mark_undone(self, task):
        self.change_status(task, False)

    def show_tasks(self):
        for task in self.task_list.tasks:
            task.display()
