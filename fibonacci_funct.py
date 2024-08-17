def Fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
num = int(input("Enter a number:"))
print(f"Fibonacci number for {num} is", Fibonacci(num))  