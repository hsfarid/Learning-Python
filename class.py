# class Myclass:
#     x = 5
#     y = 10


# # print(Myclass)
# p1 = Myclass()
# print(p1.x, p1.y)

#__init__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"
    

    def greet(self):
        print(f"Hello, my name is {self.name}")


person1 = Person("Deeya", 24)
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
class Student(Person):
    def __init__(self, name, age, student_id, graduationyear):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.student_id = student_id
        self.graduationyear = graduationyear

    def welcome(self):
        print(f"{self.name}, welcome to the class of {self.graduationyear}")

student1 = Student("Rash", 26, 9281717, 2020)
student1.greet()
print(student1.name, student1.student_id, student1.graduationyear)
student1.welcome()

