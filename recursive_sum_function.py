def mysum(number):
    if number == 1:
        return 1
    else:
        return mysum(number-1) + number
    
n = int(input("Enter a number: "))
print(mysum(n))