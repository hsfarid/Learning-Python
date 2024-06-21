#creating variables in python
# x = 5
# y = "John"

# print(x)
# print(y)

#variables do not need to be declared with any type
#and can even change type after they have been set
# x = 4
# x = "Reed"
# print(x)

#CASTING
#if you want to specify the data type of a variable
#this can be done with casting
# x = str(3)
# y = int(3)
# z = float(3)
# print(x, y, z)
# print(type(x), type(y), type(z))

#ASSIGN MULTIPLE VALUES
# x,y,z = "Orange", "Banana", 'Mango'
# print(x, y, z)

#ONE VALUE TO MULTIPLE VARIABLES
# x = y = z = "Orange"
# print(x, y, z)

#UNPACK A COLLECTION
#if you have a collection of values in a list, tuples etc. Python allows you to extract the values into variables. 
#This is called unpacking

# fruits = ["apple", "banana", "Orange"]
# x, y, z = fruits
# print(x, y, z)

#OUTPUT VARIABLES
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)
# print(x + "" + y + "" + z)

#GLOBAL VARIABLES
#Global variables ar variables created outside of a function
#They can be used or accessed by everyone,  both inside of functions and outside
# x = "awesome"

# def myFunc():
#     print('Python is ' + x)

# myFunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.
# x = "awesome"

# def myFunc():
#     x = "fantastic"
#     print("Python is " + x)
# myFunc()
# print("Python is " + x)

#GLOBAL KEYWORD
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

x = "awesome"

def myFunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myFunc()
print("Python is " + x)