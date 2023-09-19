# step 4.9
class Person:
    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


# step 4.10.6

class Device:
    __slots__ = '_name', '_location', '_status'

    def __init__(self, name, location, status='ON'):
        self._name = name
        self._location = location
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def turn_on(self):
        self.status = 'ON'

    def turn_off(self):
        self.status = 'OFF'


class Light(Device):
    __slots__ = '_brightness', '_color'

    def __init__(self, name, location, brightness, color):
        super().__init__(name, location)
        self._brightness = brightness
        self._color = color

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = value

    @property
    def color(self):
        return self._color

class Thermostat(Device):
    __slots__ = "_current_temperature", "_target_temperature"

    def __init__(self, name, location, current_temperature, target_temperature):
        super().__init__(name, location)
        self._current_temperature = current_temperature
        self._target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, value):
        self._current_temperature = value

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        self._target_temperature = value

class SmartTV(Device):
    __slots__ = '_channel'

    def __init__(self, name, location, channel):
        super().__init__(name, location)
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value