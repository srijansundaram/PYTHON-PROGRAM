class Employee:
    @staticmethod
    def greet():
        print("Good Morning, Sir")

gagan = Employee()
gagan.greet()

#  sometimes we need a function that doesn't use the self parameter.
#  we can define static method like this.