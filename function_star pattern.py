# n = 4
# for i  in range(n):
#     print("*" * (i+1))

# for i in range(n):
#         print(" " * (n-i-1), end="")
#         print("*" * (2*i+1), end="")
#         print(" " * (n-i-1))

# for i in range(n):
#     print("*" * (n-i))

# Using functions:

def star_pattern(n):
    for i  in range(n):
        print("*" * (i+1))

    for i in range(n):
        print(" " * (n-i-1), end="")
        print("*" * (2*i+1), end="")
        print(" " * (n-i-1))

    for i in range(n):
        print("*" * (n-i))

print(star_pattern(5))