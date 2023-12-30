num = int(input("Enter the number: "))
prime = True
for i in range(2, num):
    if num%i == 0:
        prime = False
        break
if prime:
    print(num, "is prime")
else:
    print(num, "is not prime")