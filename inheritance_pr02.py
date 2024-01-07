class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow!")

d = Dog()
d.bark()
print(d.color)
print(d.animalType)