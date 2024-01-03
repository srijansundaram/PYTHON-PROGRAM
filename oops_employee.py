class Employee:
    company = "Google"

faisal = Employee()
gagan = Employee()
faisal.salary = 3000000
gagan.salary = 3000400

print(faisal.company)
print(gagan.company)
print(faisal.salary)
print(gagan.salary)

Employee.company = "Youtube"

print(faisal.company)
print(gagan.company)