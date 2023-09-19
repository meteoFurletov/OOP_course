import math

class Pizza:
    def __init__(self, diameter):
        self.diameter = diameter

    def area_of_circle(self):
        radius = self.diameter / 2
        area = math.pi * radius ** 2
        return area

small = Pizza(25)
medium = Pizza(30)
large = Pizza(35)

print(small.area_of_circle())
print(medium.area_of_circle())
print(large.area_of_circle())

from enum import Enum
class Semaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    RED = 4


print(Semaphore.RED.value)