# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))

# if(num1>num2 and num1>num3 and num1>num4):
#     print(str(num1)+ "is GOAT.\n")
# elif(num2>num3 and num2>num4):
#     print(str(num2)+ "is GOAT.\n")
# elif(num3>num4):
#     print(str(num3)+ "is GOAT.\n")
# else:
#     print(str(num4)+ "is GOAT.\n")

# Using Functions:
def max(num1, num2, num3):
    if num1>num2:
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
        
m = max(3, 53, 5)
print(m)