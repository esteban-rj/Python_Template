#tuples are used to store multiple items in a single variable.
#tuples are ordered, immutable, and allow duplicate values.

#syntax
#tuple = (item1, item2, item3)

#example
tuple_fruits = ("apple", "banana", "cherry")
print(tuple_fruits)

#mofify tuples
#tuples are immutable, so we cannot modify the items after the tuple is created.
#but we can convert the tuple to a list, modify the list, and convert the list back to a tuple.

#example
print("modify tuples")
tuple_fruits = ("apple", "banana", "cherry")
print(tuple_fruits)


list_fruits = list(tuple_fruits)
list_fruits[0] = "orange"
tuple_fruits = tuple(list_fruits)
print(tuple_fruits)


#add items to tuple
#we can convert the tuple to a list, add the item, and convert the list back to a tuple.

#example
print("add items to tuple")
tuple_fruits = ("apple", "banana", "cherry")
print(tuple_fruits)

list_fruits = list(tuple_fruits)
list_fruits.append("orange")
tuple_fruits = tuple(list_fruits)
print(tuple_fruits)

#remove items from tuple
#we can convert the tuple to a list, remove the item, and convert the list back to a tuple.

#example
print("remove items from tuple")
tuple_fruits = ("apple", "banana", "cherry")
print(tuple_fruits)

list_fruits = list(tuple_fruits)
list_fruits.remove("banana")
tuple_fruits = tuple(list_fruits)
print(tuple_fruits)

#unpack tuples
#we can unpack the tuple into variables.

#example
print("unpack tuples")
tuple_fruits = ("apple", "banana", "cherry")
(green, yellow, red) = tuple_fruits
print(green)
print(yellow)
print(red)

