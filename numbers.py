#python numbers
#there are three numeric types in python

#int, float, and complex
#Variables of numeric types are created when you assign a value to them:
# x = 1
# y = 4.8
# z = 1j
#To verify the type of any object in Python, use the type() function:
# print(type(x))
# print(type(y))
# print(type(z))

#INT
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# x = 1
# y = 347775839653611
# z = -23565
# print(type(x))
# print(type(y))
# print(type(x))

#FLOAT
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# x = 1.0
# y = 1.10
# z = -45.34

# print(type(x))
# print(type(y))
# print(type(z))
#Float can also be scientific numbers with an "e" to indicate the power of 10.

#COMPLEX
#Complex numbers are written with a "j" as the imaginary part:
# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

#TYPE CONVERSION
#You can convert from one type to another with the int(), float(), and complex() methods:

#RANDOM NUMBER
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1, 10))
