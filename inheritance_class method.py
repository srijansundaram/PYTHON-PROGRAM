class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

# This will not change the class attribute. This will only change the instance or object attribute
    # def changeSalary(self, sal):
    #     self.salary = sal

#  So to change the class atribute
    
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(420)
print(e.salary) 
print(Employee.salary) 
