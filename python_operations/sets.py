#sets are unordered and unindexed.
#sets are mutable.
#sets are unordered.
#sets are unindexed.
#sets are unordered.

#syntax
#set = {item1, item2, item3}

#example    

set_fruits = {"apple", "banana", "cherry", "cherry"}
print(set_fruits)

#get the length of a set
#we can use the len() function to get the length of a set.

#example
print("length of a set")
set_fruits = {"apple", "banana", "cherry", "cherry"}
print(len(set_fruits))

#add items to a set
#we can use the add() function to add an item to a set.

#example
print("add items to a set")
set_fruits = {"apple", "banana", "cherry"}
set_fruits.add("orange")
print(set_fruits)

#add multiple items to a set
#we can use the update() function to add multiple items to a set.

#example
print("add multiple items to a set")
set_fruits = {"apple", "banana", "cherry"}
set_fruits.update(["orange", "mango", "pineapple"])
print(set_fruits)

#remove items from a set
#we can use the remove() function to remove an item from a set.

#example
print("remove items from a set")
set_fruits = {"apple", "banana", "cherry"}
set_fruits.remove("banana")
print(set_fruits)

#we can also use the discard() function to remove an item from a set. Discard() function does not raise an error if the item is not found.

#example
print("discard items from a set")
set_fruits = {"apple", "banana", "cherry"}
set_fruits.discard("banana")
print(set_fruits)

