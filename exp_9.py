def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result of {num1} divided by {num2} is {result}."

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except IOError:
        return "Error: An IOError occurred."
    finally:
        print("File operation attempted.")

def main():
    # Division example
    num1 = 10
    num2 = 0
    print(divide_numbers(num1, num2))

    # File read example
    filename = "non_existent_file.txt"
    print(read_file(filename))

if __name__ == "__main__":
    main()
