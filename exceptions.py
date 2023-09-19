# step 5.1.13
class Wallet:
    def __init__(self, currency, balance):
        if isinstance(currency, str) and currency.isupper() and len(currency) == 3:
            self.currency = currency
            self.balance = balance
        elif not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif isinstance(currency, str) and not len(currency) == 3:
            raise NameError("Неверная длина названия валюты")
        elif isinstance(currency, str) and not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.balance = balance

    def __eq__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return self.balance == other.balance
        elif isinstance(other, Wallet) and not self.currency == other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        elif not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")

    def __add__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance + other.balance)
        elif not isinstance(other, Wallet):
            raise ValueError("Данная операция запрещена")

    def __sub__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance - other.balance)
        elif not isinstance(other, Wallet):
            raise ValueError("Данная операция запрещена")

# step 5.3.6
try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a / b}")
except (ValueError, ZeroDivisionError):
    print('Введите корректные значения')

# step 5.3.7
try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a / b}")
except ValueError:
    print('Введите целое число')
except ZeroDivisionError:
    print('Делитель не должен быть равен нулю')

# step 5.3.14

try:
    file = open('pentagon_secrets.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print("Эх, не судьба тайны пентагона узнать")

#step 5.3.15

def func(phrase):
    func(phrase)

try:
    func('Это рекурсия, детка!')
except RecursionError:
    print("Кто-то должен остановить это безумиe")

from enum import Enum


