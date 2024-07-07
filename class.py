# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.move()

# point2 = Point(10, 20)
# print(point2.x)

# class Person:
#     #constructor
#     def __init__(self, name):
#         self.name = name
    
#     def talk(self):
#         print(f"Hey! I am {self.name}.")


# Reed = Person("Reed")
# Rashid = Person("Rashid")
# print(Reed.name, Rashid.name)
# Reed.talk()
# Rashid.talk()

#inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print('bark')
    

class Cat(Mammal):
    pass

dog1 = Dog()
cat1 = Cat()

dog1.walk()
dog1.bark()
cat1.walk()

