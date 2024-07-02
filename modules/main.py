#import modules
from calculator import add
from calculator import sub
from calculator import multiply
from calculator import divide

#accept two numbers from a user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#perform calculations
# add = calculator.add(num1, num2)
add = add(num1, num2)
sub = sub(num1, num2)
multiply = multiply(num1, num2)
divide = divide(num1, num2)

#display results
print(f"The sum of {num1} and {num2} is: {add}")
print(f"The difference betweem {num1} and {num2} is: {sub}")
print(f"The product of {num1} and {num2} is: {multiply}")
print(f"The division of {num1} and {num2} is: {divide}")