#enumerate and zip

#enumerate
#enumerate is a function that returns an enumerate object.

#example
print("enumerate")
fruits = ["apple", "banana", "cherry"]
for x in enumerate(fruits):
    print(x)

#zip
#zip is a function that returns a zip object.

#example
print("zip")
index = [1, 2, 3]
fruits = ["apple", "banana", "cherry"]
for x in zip(index, fruits):
    print(x)