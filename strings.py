#PYTHON STRINGS
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
print("hello")
print('hello')

#QUOTES INSIDE QUOTES
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("I'm Fareed")
print('My name is "Fareed"')

#ASSIGNING STRING TO A VARIABLE
a= "hello"
print(a)

#MULTILINE STRINGS
#You can assign a multiline string to a variable by using three quotes:

a = """
My name is Fareed, I come from Ghana.
I love coding and playing football.
"""
print(a)

#STRINGS ARE ARRAYS
a = "Hello, world"
print(a[1])

#LOOPING THROUGH A STRING
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
a = "banana"
for x in a:
    print(x)
    
#STRING LENGTH
#To get the length of a string, use the len() function.
a = "banana"
print(len(a))

#CHECK STRING
#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free"
print('free' in txt)
# Use it in an if statement:
if "free" in txt:
    print("YES, 'free' is present.")

#CHECK IF NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
a = "hello world"
print("free" not in a)

txt = "The best things in the world are free"
if 'bad' not in txt:
    print("No, 'bad' is not present.")


#SLICING STRINGS
name = "Fareed"
#slice from start
print(name[0:4])
print(name[:4])
#slice to the end
print(name[0:])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
print(name[-4:-3])
print(name[-3:-2])

# MODIFY STRINGS
#TO UPPER CASE AND LOWER CASE
a = "hello world"
b = "HELLO WORLD"
print(a.upper())
print(b.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text,
# and very often you want to remove this space.
a = " Hello, World! "
print(a.strip())

#REPLACE STRING
# The replace() method replaces a string with another string:
print(a.replace('H', "F"))

#SPLIT STRINGS
print(a.split(','))

# STRING CONCATENATION
# To concatenate, or combine, two strings you can use the + operator.
a = 'My name is '
b = 'Fareed'
print(a + b)

# FORMAT STRINGS
name = "Fareed"
age = 27
print("My name is ", name, "I am ", age, "years old.")
print("My name is " + name)

# F-STRINGS
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
print(f"My name is {name}. I am {age} years old.")

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.
price  = 67
print(f"The price is ${price}")
print(f"The price is ${price:.2f}")

#ESCAPE CHARACTERS
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
a = "We are the so-called \"Vikings\" from \nthe north"
print(a)

# STRING METHODS
a  = "Hello World"
print(a.capitalize())
print(a.count('o'))
print(a.casefold())
print(a.lower())
print(a.endswith('d'))

