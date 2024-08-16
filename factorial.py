# num = int(input("Enter a number: "))
# result = 1
# if num < 0:
#     print("Number is negative")
# else:
#     for i in range(1, num + 1):
#         result *= i
#     print (result)

# Using while loop:
num = int(input("Enter a number: "))
result = 1
i =1
while i <= num:
    result *= i
    i +=1
print(result)