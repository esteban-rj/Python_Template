from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def say_hello(self):
        return NotImplemented

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age