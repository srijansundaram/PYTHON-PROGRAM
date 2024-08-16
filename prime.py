num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number")
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) +1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")

# Using while loop:
else:
    i = 2
    is_prime = True
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i +=1
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")