#Parent class/Super class/Base class

class Animal:

       isManual = True
       age = 5

       def movement(self):
           print("Animal is moving")

#Child class/Sub class/Dwrived class
class Dog(Animal):
    def bark(self):
        print("Woof! Woof! Woof!")


class Cat(Animal):
    def meow(self):
        print("Meow! Meow!")

dog1 = Dog()
dog1.movement()
print(dog1.age)

cat1 = Cat()
cat1.meow()
