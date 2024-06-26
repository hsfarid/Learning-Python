# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# List Items
# List items are ordered, changeable, and allow duplicate values.

#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

#If you add new items to a list, the new items will be placed at the end of the list.

#Note: There are some list methods that will change the order, but in general: the order of the items will not change.

#Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:

cars  = ["benz", "volvo", "fiat", "toyota"]
#print lists
print(cars)
#print individual items using index
print(cars[2])
#change items
cars[3] = "bmw"
#change a range of item values
cars[1:3] = ["acura","range rover" ]
#length of the list
print(len(cars))
#type of the list
print(type(cars))
#indexing
print(cars[:4])
print(cars[0:])
#negative indexing
print(cars[-3:])
print(cars[-4:-1])

#check if items exist
if "bmw" in cars:
    print("YES it is present")
else:
    print("NO it is not present")

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:
print(cars)
cars.insert(2, "jeep")
cars.insert(-1, "bugatti")
print(cars)

# Append Items
# To add an item to the end of the list, use the append() method:
cars.append("ferrari")
print(cars)

# Extend List
# To append elements from another list to the current list, use the extend() method.
cars_update = ["pajero", "porshe", "tesla"]
cars.extend(cars_update)
print(cars)

# Remove Specified Item
# The remove() method removes the specified item.
cars.remove("tesla")
print(cars)

# Remove Specified Index
# The pop() method removes the specified index.
#If you do not specify the index, the pop() method removes the last item.
# cars.pop(5)
# print(cars)
# The del keyword also removes the specified index:
# del cars[2]
# print(cars)
#the del keyword can also delete the entire list
# del cars
# print(cars)

#clear the list
# cars.clear()
# print(cars)

#LOOPING THROUGH LISTS
# for car in cars:
#     print(car)

# for i in range(len(cars)):
#     print(cars[i])

#Using while loop
# i = 0
# while i < len(cars):
#     print(cars[i])
#     i += 1

#List comprehension
[print(car) for car in cars]

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "cherry", "banana", "mango", "pineaple", "grapes"]
newList = []

# for fruit in fruits:
#     if "a" in fruit:
#         newList.append(fruit) 
# print(newList)

# With list comprehension you can do all that with only one line of code:
# newList = [fruit for fruit in fruits if "a" in fruit]

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
# Condition
# The condition is like a filter that only accepts the items that valuate to True.
# newlist = [fruit for fruit in fruits]
# print(newlist)
# newlist = [fruit for fruit in fruits if fruit != "apple"]
# print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
newlist = [fruit.upper() for fruit in fruits]
print(newlist)
