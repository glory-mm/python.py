#Enhances multiple classes with the same method name

class car:

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def move(self):
        print("drive!")


car1 = car("red", "Ford", "2016")
print(car1.color)