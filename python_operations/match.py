#match switch

#match is a function that returns a match object.

#example
print("match")
x = 1
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case _:
        print("x is not 1 or 2")    

#match case with multiple conditions
#we can use multiple conditions in a match case by using the | operator.

#example
print("match case with multiple conditions")
x = 1
match x:
    case 1 | 2:
        print("x is 1 or 2")
    case 3:
        print("x is 3")
    case _:
        print("x is not 1, 2, or 3")

#match case with range
#we can use a range in a match case by using the range() function.

#example
print("match case with range")
x = 5
match x:
    case x if x > 0 and x < 10:
        print("x is between 0 and 10")
    case x if x > 10 and x < 20:
        print("x is between 10 and 20")
    case _:
        print("x is not between 0 and 20")

#match case with multiple ranges
#we can use multiple ranges in a match case by using the | operator.

#example
print("match case with multiple ranges")
x = 15
match x:
    case x if x > 0 and x < 10:
        print("x is between 0 and 10")
    case x if x > 10 and x < 20:
        print("x is between 10 and 20")
    case x if x > 20 and x < 30:
        print("x is between 20 and 30")
    case _:
        print("x is not between 0 and 30")
