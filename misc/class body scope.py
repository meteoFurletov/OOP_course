# step 6
"""Создайте класс Robot, у которого есть:

атрибут класса population. В этом атрибуте будет храниться общее количество роботов,
 изначально принимает значение 0;
 
конструктор __init__, принимающий 1 аргумент name. Данный метод должен сохранять
 атрибут name и печатать сообщение вида "Робот <name> был создан". 
 Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
 
метод destroy, должен уменьшать популяцию роботов на единицу и 
печатать сообщение вида "Робот <name> был уничтожен"
 
метод say_hello, которой печатает сообщение вида "Робот <name> 
приветствует тебя, особь человеческого рода"
 
метод класса  how_many, который печатает сообщение вида "<population>, 
вот сколько нас еще осталось"""


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        self.create()

    def create(self):
        Robot.population += 1
        print(f"Робот {self.name} был создан")

    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")


# step 10

""" Создайте базовый класс User, у которого есть:

метод __init__, принимающий имя пользователя и его роль.
 Их необходимо сохранить в атрибуты экземпляра name и role соответственно
Затем создайте класс Access , у которого есть:

приватный атрибут класса __access_list , в котором хранится список ['admin', 'developer']
 
приватный статик-метод __check_access , который принимает название 
роли и возвращает True, если роль находится в списке __access_list , иначе - False
 
публичный статик-метод get_access , который должен принимать 
экземпляр класса User и проверять есть ли доступ у данного пользователя 
к ресурсу при помощи метода __check_access  . Если у пользователя достаточно 
прав, выведите на экран сообщение
«User <name>: success», если прав недостаточно - «AccessDenied»
Если передается тип данных, отличный от экземпляр класса User, необходимо вывести сообщение:
«AccessTypeError»
"""


class User:
    def __init__(self, username, role):
        self.name = username
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        if role in Access.__access_list:
            return True
        else:
            return False

    @staticmethod
    def get_access(user):
        if isinstance(user, User):
            if Access.__check_access(user.role):
                print(f'User {user.name}: success')
            else:
                print(f'AccessDenied')
        else:
            print('AccessTypeError')


user1 = User('batya99', 'admin')
Access.get_access(user1)  # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya)  # печатает AccessDenied

Access.get_access(5)  # печатает AccessTypeError

# step 11
"""Создайте класс BankAccount, который имеет:

атрибут класса bank_name со значением "Tinkoff Bank"
 
атрибут класса address со значением  "Москва, ул. 2-я Хуторская, д. 38А"
 
метод __init__, который устанавливает значения атрибутов
 name и balance : владелец счета и значение счета
 
класс метод create_account, который возвращает новый 
экземпляр класса BankAccount. Метод принимает имя клиента и сумму взноса
 
класс метод bank_info, который возвращает информация о банке в виде:
«{bank_name} is located in {address}»"""

class BankAccount:
    bank_name = "Tinkoff Bank"
    address = "Москва, ул. 2-я Хуторская, д. 38А"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, balance):
        return BankAccount(name, balance)

    @classmethod
    def bank_info(cls):
        return f'{cls.bank_name} is located in {cls.address}'
