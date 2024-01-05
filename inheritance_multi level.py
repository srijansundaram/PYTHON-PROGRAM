class Person:
    country = "India"

    def takeBreak(self):
        print("I am breathing...")
    
class Employee:
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am an employee..")

class programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
      print(f"No salary to programmer")  

    # def takeBreak(self):
    #     print("I am programmer")

p = Person()
e = Employee()
pr = programmer()

p.takeBreak()
e.takeBreak()
pr.takeBreak() # this will print the class attributes of the nearest parent as it doesn't have take break attribute

