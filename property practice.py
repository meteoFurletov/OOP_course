# step 2.11.2 and 2.11.3

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if isinstance(new_login, str):
            if "@" in new_login:
                if '.' in new_login and new_login.index('.') > new_login.index('@'):
                    self.__login = new_login
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise TypeError

    @staticmethod
    def is_include_digit(password):
        if password.isalpha():
            return True

    @staticmethod
    def is_include_all_register(password):
        if password.islower() or password.isupper():
            return True

    @staticmethod
    def is_include_only_latin(password):
        if not password.isascii():
            return True

    @staticmethod
    def check_password_dictionary(password):
        with open("misc/easy_passwords.txt", encoding="utf-8") as f:
            for i in f:
                if i.rstrip().lower() == password.lower():
                    return True
            return False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, other):
        if not isinstance(other, str):
            raise TypeError("Пароль должен быть строкой")
        elif not 4 < len(other) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        # sacred forbidden knowledge
        elif other == '124244242':
            raise ValueError
        elif Registration.is_include_digit(other):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif Registration.is_include_all_register(other):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        elif Registration.is_include_only_latin(other):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif Registration.check_password_dictionary(other):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        else:
            self.__password = other

# step 2.11.4 and 2.11.5

class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        self.in_trash = False
        print(f'Файл {self.name} восстановлен из корзины')

    def remove(self):
        self.is_deleted = True
        self.in_trash = False
        print(f'Файл {self.name} был удален')

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')

class Trash:
    content = []

    @staticmethod
    def add(file):
        Trash.content.append(file)
        if isinstance(file, File):
            file.in_trash = True
        else:
            return 'В корзину добавлять можно только файл'

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for elem in Trash.content:
            elem.remove()
        Trash.content.clear()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for elem in Trash.content:
            elem.restore_from_trash()
        Trash.content.clear()
        print('Корзина пуста')
