# step 3
"""Создайте класс UnitedKingdom, у которого необходимо реализовать:

статический метод get_capital, который печатает строку "London is the capital of Great Britain."
статический метод get_language, который печатает строку
 "English is the primary language of Great Britain."
Создайте класс Spain, у которого необходимо реализовать:

статический метод get_capital, который печатает строку "Madrid is the capital of Spain."
статический метод get_language, который печатает строку "Spanish is the primary language of Spain."
Код ниже под реализациями классов удалять не нужно"""


class UnitedKingdom:
    @staticmethod
    def get_capital():
        print("London is the capital of Great Britain.")

    @staticmethod
    def get_language():
        print("English is the primary language of Great Britain.")


class Spain:
    @staticmethod
    def get_capital():
        print("Madrid is the capital of Spain.")

    @staticmethod
    def get_language():
        print("Spanish is the primary language of Spain.")


obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.get_capital()
    country.get_language()
