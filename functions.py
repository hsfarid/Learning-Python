#functions that carry out a task
#functions that returns a value

def greet(name):
    print(f"Hi, {name}")

print(greet("Reed"))

result = greet('Reed')
print(result)

#keyword arguments
def increment(number, by):
    return number + by

result = increment(4, 2)
print(result)

#keyword arguments makes the function call more readable
print(increment(number=2, by=1))

#default parameters
def increment(number, by=3):
    return number + by

print(increment(2)) #if second argument is passed, it will overwrite the default parameter
#optional or default parameters should come after required parameters

# *args - tuples
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3, 4, 5))

# **args - dictionaries
def save_user(**user):
    print(user["name"])
save_user(id=1, name="Reed", age=27)

#scope - local variable, global variable, global keyword

message = "b"
def greet():
    global message
    message = "a" #local variable

greet()
print(message)