#PYTHON STRINGS
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
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
#Use it in an if statement:
if "free" in txt:
    print("YES, 'free' is present.")

#CHECK IF NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
a = "hello world"
print("free" not in a)

txt = "The best things in the world are free"
if 'bad' not in txt:
    print("No, 'bad' is not present.")