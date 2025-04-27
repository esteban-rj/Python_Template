#lists are ordered and mutable.
#lists are indexed.
#lists are mutable.

#syntax
#list = [item1, item2, item3]

#example
list_fruits = ["apple", "cherry", "banana"]
print(list_fruits)

#get the length of a list
#we can use the len() function to get the length of a list.

#example
print("length of a list")
list_fruits = ["apple", "cherry", "banana"]
print(len(list_fruits))

#access items in a list
#we can access items in a list by their index.

#example
print("access items in a list")
list_fruits = ["apple", "cherry", "banana"]
print(list_fruits[0])
print(list_fruits[1])
print(list_fruits[2])

#negative indexing
#we can also access items in a list by their negative index.

#example
print("negative indexing")
list_fruits = ["apple", "cherry", "banana"]
print(list_fruits[-1])
print(list_fruits[-2])
print(list_fruits[-3])

#range of indexes
#we can also access items in a list by their range of indexes.

#example
print("range of indexes")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
print(list_fruits[2:5])

#range of negative indexes
#we can also access items in a list by their range of negative indexes.

#example
print("range of negative indexes")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
print(list_fruits[-5:-2])

#check if an item exists in a list
#we can use the in keyword to check if an item exists in a list.

#example
print("check if an item exists in a list")
list_fruits = ["apple", "cherry", "banana"]
if "apple" in list_fruits:
    print("Yes, apple is in the list")
else:
    print("No, apple is not in the list")

#change  item value
#we can change the value of an item in a list by its index.

#example
print("change item value")
list_fruits = ["apple", "cherry", "banana"]
list_fruits[1] = "orange"
print(list_fruits)

#change a range of item values
#we can change the value of a range of items in a list by their range of indexes.   
#example
print("change a range of item values")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits[1:3] = ["kiwi", "mango"]
print(list_fruits)

#insert items
#we can insert an item into a list by its index.

#example
print("insert items")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.insert(2, "kiwi")
print(list_fruits)

#add items
#we can add an item to the end of a list by using the append() function.

#example
print("add items")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.append("kiwi")
print(list_fruits)

#add items to the end of a list
#we can add an item to the end of a list by using the extend() function.

#example
print("add items to the end of a list")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.extend(["kiwi", "mango"])
print(list_fruits)

#remove items
#we can remove an item from a list by using the remove() function.

#example
print("remove items")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.remove("banana")
print(list_fruits)

#remove items by index
#we can remove an item from a list by its index by using the pop() function.

#example
print("remove items by index")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.pop(2)
print(list_fruits)

#remove the last item
#we can remove the last item from a list by using the pop() function.

#example
print("remove the last item")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.pop()
print(list_fruits)

#clear a list
#we can clear a list by using the clear() function.

#example
print("clear a list")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.clear()
print(list_fruits)

#loop through a list
#we can loop through a list by using a for loop.

#example
print("loop through a list")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
for x in list_fruits:
    print(x)

#loop through the index numbers
#we can loop through the index numbers of a list by using the range() function.

#example
print("loop through the index numbers")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
for i in range(len(list_fruits)):
    print(list_fruits[i])

#while loop
#we can loop through a list by using a while loop.

#example
print("while loop")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
i = 0
while i < len(list_fruits):
    print(list_fruits[i])
    i += 1

#sort a list
#we can sort a list by using the sort() function.

#example
print("sort a list")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.sort()
print(list_fruits)

#sort a list in descending order
#we can sort a list in descending order by using the sort() function and passing the reverse=True argument.

#example
print("sort a list in descending order")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits.sort(reverse=True)
print(list_fruits)

#copy a list
#we can copy a list by using the copy() function.

#example
print("copy a list")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits2 = list_fruits.copy()
print(list_fruits2)

#join two lists
#we can join two lists by using the + operator.

#example
print("join two lists")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits2 = ["kiwi", "mango"]
list_fruits3 = list_fruits + list_fruits2
print(list_fruits3)

#join two lists by using the extend() function.

#example
print("join two lists by using the extend() function")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
list_fruits2 = ["kiwi", "mango"]
list_fruits.extend(list_fruits2)
print(list_fruits)

#list comprehension
#we can create a new list by using a list comprehension.

#example
print("list comprehension")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
newlist = [x for x in list_fruits if x != "apple"]
print(newlist)

#count an item in a list
#we can count an item in a list by using the count() function.

#example
print("count an item in a list")
list_fruits = ["apple", "cherry", "banana", "orange", "mango"]
print(list_fruits.count("apple"))