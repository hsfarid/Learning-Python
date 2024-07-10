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