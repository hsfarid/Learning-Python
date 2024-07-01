length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

def area_rectangle(length, width):
    return length * width
area = area_rectangle(length, width)
print(f"The area of the rectangle is: {area} sq units.")