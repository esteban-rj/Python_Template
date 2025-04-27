from user import User
from singleton_drink import Drink

if __name__ == "__main__":
    user = User("John", 25, "john@example.com")
    print(user.say_hello())
    user.drink(Drink("Water"))

    user2 = User("Jane", 30, "jane@example.com")
    print(user2.say_hello())
    user2.drink(Drink("Water"))
    