from person import Person
from singleton_drink import Drink
class User(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self._email = email
    
    def say_hello(self):
        return f"Hello, my name is {self._name} and I am {self._age} years old. My email is {self._email}."
    
    def drink(self, drink: Drink):
        print(f"{self._name} is drinking {drink.name}")
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email