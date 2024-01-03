class Calculator:
    @staticmethod
    def greet():
        print("Hello, What you want to calculate??")
    def __init__(self, num):
        self.number = num
    def square(self):
        print(f"The value of square of {self.number} is {self.number **2}")
    
    def squareroot(self):
        print(f"The value of square root of {self.number} is {self.number **0.5}")
    
    def cube(self):
        print(f"The value of cube of {self.number} is {self.number **3}")

a = Calculator(num=int(input("Enter a number: ")))
a.greet()

b = input("Press 's' for square, 'sr' for square root and 'c' for cube: ")

if b == 's' or b == 'S':
    a.square()

elif b == 'sr' or b == 'Sr' or b == 'SR' or b == 'sR':
    a.squareroot()
elif b == 'c' or b == 'C':
    a.cube()
else:
    print("Invalid input.")

    