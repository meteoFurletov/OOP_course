# step 6
class Square:
    def get_value(self, a):
        return a * a


class Cube(Square):
    def get_value(self, a):
        return a ** 3


class Power4(Square):
    def get_value(self, a):
        return a ** 4
