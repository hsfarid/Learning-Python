number = int(input("Enter an integer: "))

def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
even_or_odd(number)