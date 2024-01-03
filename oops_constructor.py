class Employee:
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print(f"Employee is created with name {self.name} having salary {self.salary} in {self.subunit} subunit.")

gagan = Employee("gagan", 100, "YouTube")
