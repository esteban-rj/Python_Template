import random

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Drink(metaclass=SingletonMeta):
    def __init__(self, name):
        self._name = name + str(random.randint(0, 1000))

    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name