# Class is a blueprint of an object
# Object is an instance of a class

class Employee:

    def __init__(self, name, gender,position, age):
        self.name = name
        self.gender = gender
        self.position = position
        self.age = age

    def drive(self):
        print("Employee is driving")

    def eat(self):
        print("Employee is eating")



employee1 = Employee("Mary", "Female", "HR", 43) #Creating objects
print(employee1.name, employee1.gender, employee1.position, employee1.age)
employee1.drive()
employee1.eat()

employee2 = Employee("Peter", "Male", "Manager", 56)
print(employee2.name, employee2.gender, employee2.age)
employee2.drive()
employee2.eat()

employee3 = Employee("Joyce", "Female", "Secretary", 25)
print(employee3.name, employee3.gender, employee3.age)
employee3.drive()
employee3.eat()