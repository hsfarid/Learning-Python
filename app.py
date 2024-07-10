class Dog:
    def __init__ (self, name):
        self.name = name
    def bark (self):
        print ("bark")
    
    def walk (self):
        print ('walk')


dog1 = Dog("bob")
print(dog1.name)
dog1.bark()
dog1.walk()

class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def display_info(self):
        print(f"Student name: {self.name}, Student age: {self.age}")

student1 = Student("Reed", 27)
student1.display_info()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        total_value = self.price * self.quantity
        print(f"The total value of stock for {self.name} is {total_value}")
    

product1 = Product('Burkina', 3, 50)
product1.total_value()

#EXCEPTIONS
#example1
def add(x, y):
    try:
        return x / y
    
    except ZeroDivisionError as e:
        # print("Sorry, cannot divide by zero.")
        # return "Sorry, cannot divide by zero."
        return e

result = add(10, 0)
print(result)

#example2
try:
    with open('test_fle.txt', 'r') as f:
        read_data = f.read()
    print(read_data)
except Exception as e:
    print(e)

#example3
class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"sorry, {self.number} is greater than 100."


number = int(input("Enter number: "))
def input_number(number):
    try:
        if number > 100:
            raise ValueTooHighError(number) 
        else:
            print(f"The number is: {number}")
    except TypeError:
        print("Enter an int")

try:
    input_number(number)
    # input_number(105)
except ValueTooHighError as e:
    print(e)
    




    



