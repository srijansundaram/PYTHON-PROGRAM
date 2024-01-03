class Employee:
    company = "Google"
    def getsalary(self, signature):
        # print("Salary is 100K")
        print(f"Salary for this employee workin in {self.company} is {self.salary}\n{signature}")

gagan = Employee()
gagan.salary = 1584896
gagan.getsalary("Thanks.") # Employee.getsalary(gagan)
# here gagan is self
#  self is a parameter which get passed automatically with a function call from an object