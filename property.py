# step 2.5.9

class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def __calculate_average(self):
        total = sum(self.numbers)
        return total / len(self.numbers)


average_calculator = AverageCalculator([1, 2, 3])
print(average_calculator._AverageCalculator__calculate_average())

# step 2.5.10

class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass


maker = PizzaMaker()
maker._make_barbecue()
maker._PizzaMaker__make_pepperoni()

# step 2.5.11

class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f"Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}")

    def access_private_method(self):
        self.__display_details()


# step 2.5.12

class BankDeposit:
    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance * (self.rate / 100)

    def get_balance_with_profit(self):
        return self.balance + (self.__calculate_profit())

# step 2.5.13

class Library:
    def __init__(self, books):
        self.__books = books

    def __check_availability(self, book):
        return True if book in self.__books else False

    def search_book(self, book):
        return self.__check_availability(book)

    def return_book(self, book):
        self.__books.append(book)

    def _checkout_book(self, book):
        if self.__check_availability(book):
            self.__books.remove(book)
            return True

        else:
            return self.__check_availability(book)


# step 2.5.14

class Employee:
    def __init__(self, name, position, hours, rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours
        self.__hourly_rate = rate

    def __calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    def _set_position(self, new_position):
        self.__position = new_position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return (f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}")


# step 2.6.11

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

# step 2.6.14

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if (not isinstance(value, (int, float))) or value < 0:
            print(f"ErrorValue:{value}")
        else:
            self.__salary = value

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)

# step 2.6.15

class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str) and email.count('@') == 1:
            if '.' in email and email.index('.') > email.index('@'):
                self.__email = email
            else:
                print(f'ErrorMail:{email}')
        else:
            print(f'ErrorMail:{email}')

    email = property(fget=get_email, fset=set_email)


# step 2.7.9
class Celsius:
    def __init__(self, degree):
        self._temperature = degree

    def to_fahrenheit(self):
        return self._temperature * 9 / 5 + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, other):
        if other < -273.15:
            raise ValueError
        else:
            self._temperature = other


# step 2.7.10
class File:
    def __init__(self, size_in_bytes):
        self._size_in_bytes = size_in_bytes

    @property
    def size(self):
        if self._size_in_bytes < 1024:
            return f"{self._size_in_bytes} B"
        elif 1024 <= self._size_in_bytes < 1024**2:
            return f"{self._size_in_bytes/1024:.2f} KB"
        elif 1024**2 <= self._size_in_bytes < 1024**3:
            return f"{self._size_in_bytes/1024**2:.2f} MB"
        else:
            return f"{self._size_in_bytes/1024**3:.2f} GB"

    @size.setter
    def size(self, other):
        self._size_in_bytes = other

# step 2.7.12
class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for i, note in enumerate(self._notes):
            print(f'{i + 1}.{note}')


# step 2.7.16
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.total_cents % 100
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:
            self.total_cents = (self.total_cents // 100) * 100 + value
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"
