class Employee:
    salary = 15000
    increment = 2.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 25000
print(e.increment)
