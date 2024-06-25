# Booleans represent one of two values: True or False.
# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 5)
print(4 == 6)
print(5 != 3)
print(5 < 3)
print(4 >= 6)

# When you run a condition in an if statement, Python returns True or False:
# Example
# Print a message based on whether the condition is True or False:
a = 6
b = 4
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("hello"))
print(bool(13))
print(bool(False))
print(bool(-5))
print(bool(""))
print(bool(0))
print(bool(None))

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:

def myFunc() :
    return True;
print(myFunc())

# You can execute code based on the Boolean answer of a function:
def my_func():
    return True;
if my_func():
    print("YES")
else:
    print('NO')
