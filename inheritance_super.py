class Person:
    country = "India"

    def __init__(self):
        print("Initalizing person...")

    def takeBreath(self):
        print("I am breathing...")
    
class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__() 
        print("Initalizing employee...")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee..")

class programmer(Employee):
    company = "Fiverr"

    # def __init__(self):
    #     super().__init__() 
    #     print("Initalizing programmer...")

    def getSalary(self):
      print(f"No salary to programmer")  

    def takeBreath(self):
        super().takeBreath() # this wil also print the attribute of parent class
        print("I am programmer")

# p = Person()
# p.takeBreath()

# e = Employee() 
# e.takeBreath()

pr = programmer()
pr.takeBreath()