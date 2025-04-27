#create a dictionary
#we can create a dictionary by using the dict() function.

#example
print("create a dictionary")

#create a dictionary with key-value pairs
#we can create a dictionary with key-value pairs by using the dict() function.

#example
print("create a dictionary with key-value pairs")
pokedex = {
    "1": "bulbasaur",
    "2": "ivysaur",
    "3": "venusaur",
    "4": "charmander",
    "5": "charizard"
}
print(pokedex)

#access items in a dictionary
#we can access items in a dictionary by their key.

#example
print("access items in a dictionary")
print(pokedex["1"])
print(pokedex["2"])
print(pokedex["3"])
print(pokedex["4"])
print(pokedex["5"])

#get the length of a dictionary
#we can get the length of a dictionary by using the len() function.

#example
print("get the length of a dictionary")
print(len(pokedex))

#add items to a dictionary
#we can add items to a dictionary by using the update() function.

#example
print("add items to a dictionary")
pokedex.update({"6": "squirtle"})
print(pokedex)

#remove items from a dictionary
#we can remove items from a dictionary by using the pop() function.

#example
print("remove items from a dictionary")
pokedex.pop("6")
print(pokedex)

#remove the last item from a dictionary
#we can remove the last item from a dictionary by using the popitem() function.

#example
print("remove the last item from a dictionary")
pokedex.popitem()
print(pokedex)

#clear a dictionary
#we can clear a dictionary by using the clear() function.

#example
print("clear a dictionary")
pokedex.clear()
print(pokedex)


#loop through a dictionary
#we can loop through a dictionary by using a for loop.

#example
print("loop through a dictionary")
for x in pokedex:
    print(x)    

#loop through the values of a dictionary
#we can loop through the values of a dictionary by using the values() function.

#example
print("loop through the values of a dictionary")
for x in pokedex.values():
    print(x)

#loop through the keys and values of a dictionary
#we can loop through the keys and values of a dictionary by using the items() function.

#example
print("loop through the keys and values of a dictionary")
for x, y in pokedex.items():
    print(x, y)

#check if a key exists in a dictionary
#we can check if a key exists in a dictionary by using the in keyword.

#example
print("check if a key exists in a dictionary")
if "1" in pokedex:
    print("Yes, 1 is in the dictionary")
else:
    print("No, 1 is not in the dictionary")

#check if a value exists in a dictionary
#we can check if a value exists in a dictionary by using the in keyword.

#example
print("check if a value exists in a dictionary")
if "bulbasaur" in pokedex.values():
    print("Yes, bulbasaur is in the dictionary")
else:
    print("No, bulbasaur is not in the dictionary")


#copy a dictionary
#we can copy a dictionary by using the copy() function.

#example
print("copy a dictionary")
pokedex2 = pokedex.copy()
print(pokedex2)

#nesting dictionaries
#we can nest dictionaries by using the dictionary inside a dictionary.

#example
print("nesting dictionaries")
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

#dictionary methods
#we can use the following methods to manipulate dictionaries.

#example
print("dictionary methods")

#get the keys of a dictionary
#we can get the keys of a dictionary by using the keys() function.

#example
print("get the keys of a dictionary")
print(pokedex.keys())

#get the values of a dictionary
#we can get the values of a dictionary by using the values() function.

#example
print("get the values of a dictionary")
print(pokedex.values())

#get the items of a dictionary
#we can get the items of a dictionary by using the items() function.

#example
print("get the items of a dictionary")
print(pokedex.items())

#check if a dictionary is empty
#we can check if a dictionary is empty by using the len() function.

#example
print("check if a dictionary is empty")
print(len(pokedex) == 0)

#create a dictionary from two lists
#we can create a dictionary from two lists by using the zip() function.

#example
print("create a dictionary from two lists")
keys = ["1", "2", "3"]
values = ["bulbasaur", "ivysaur", "venusaur"]
pokedex3 = dict(zip(keys, values))
print(pokedex3)

#dictionary comprehension
#we can create a dictionary by using a dictionary comprehension.    

#example
print("dictionary comprehension")
pokedex4 = {x: x**2 for x in range(10)}
print(pokedex4) 

#dictionary from a list of tuples
#we can create a dictionary from a list of tuples by using the dict() function.

#example
print("dictionary from a list of tuples")
pokedex5 = dict([("1", "bulbasaur"), ("2", "ivysaur"), ("3", "venusaur")])
print(pokedex5)
