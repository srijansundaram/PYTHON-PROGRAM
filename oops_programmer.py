class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self. product = product

        print(f"Employee is created with name {self.name} in {self.product}.")
    def getinfo(self, signature):
        print(f"Salary of this employee working in {self.product} is {self.salary}\n {signature} ")

gagan = Programmer("gagan", "skype")
gagan.salary = 150065
gagan.getinfo("Thanks.")

faisal = Programmer("faisal", "github")
faisal.salary = 155931
faisal.getinfo("Thanks.")
