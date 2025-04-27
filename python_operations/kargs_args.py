#kargs and args are used to pass a variable number of arguments to a function.

#args is used to pass a variable number of arguments to a function.

#example
print("args")
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

#kargs is used to pass a variable number of keyword arguments to a function.

#example
print("kargs")
def print_person(**kwargs):
    print(kwargs)

print_person(name="John", age=25, city="New York")