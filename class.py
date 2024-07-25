# class Myclass:
#     x = 5
#     y = 10


# # print(Myclass)
# p1 = Myclass()
# print(p1.x, p1.y)

#__init__ function
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.age}"
    

#     def greet(self):
#         print(f"Hello, my name is {self.name}")


# person1 = Person("Deeya", 24)
# person2 = Person("Reed", 26)
# print(person1.name, person1.age)
# print(person2.name, person2.age)
# print(person1)
# person1.greet()
# person1.age = 25

# delete object properties
# del person1.age 
# print(person1.age)

# delete object
# del person1
# print(person1)

# python inheritance 
#example
# class Student(Person):
#     def __init__(self, name, age, student_id, graduationyear):
#         # Person.__init__(self, name, age)
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.graduationyear = graduationyear

#     def welcome(self):
#         print(f"{self.name}, welcome to the class of {self.graduationyear}")

# student1 = Student("Rash", 26, 9281717, 2020)
# student1.greet()
# print(student1.name, student1.student_id, student1.graduationyear)
# student1.welcome()

#example
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print(f"General animal sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# lassie = Dog("Lassie")
# print(lassie.name)
# lassie.make_sound()

#example
# class Bird:
#     def fly(self):
#         print("I can fly")


# class Mammal:
#     def run(self):
#         print("I can run")


# class Bat(Bird, Mammal):
#     pass


# bat = Bat()
# bat.fly()
# bat.run()

#example
# class Dog:
#     def make_sound(self):
#         return "dog sound"

# class Bird:
#     def make_sound(self):
#         return "bird sound"

# class Cat:
#     def make_sound(self):
#         return "cat sound"

# def let_them_speak(sounds):
#     for sound in sounds:
#         print(sound.make_sound())


# let_them_speak([Dog(), Cat(), Bird()])

# practice exercises 
# constructors and destructors 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def print_info(self):
#         print(f"Your name is {self.name}, and you are {self.age} years old.")
#     def __del__(self):
#         print(f"good bye, {self.name}")

# person1 = Person("Rash", 26)
# person1.print_info()


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"The book '{self.title}' has {self.pages} pages and was written by {self.author}"

#     def __repr__(self):
#         return f"The book '{self.title}' has {self.pages} pages and was written by {self.author}"
    

# book1  = Book("be obsessed or get average", "Rash", 765)
# print(book1.__repr__())
# print(book1)

#classmethods
class Person:
    count = 0

    def __init__(self, name):
        self.name = name 
        Person.count += 1
        
    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")

person1 = Person("Alice")
person2 = Person("Rick")
Person.display_count()




