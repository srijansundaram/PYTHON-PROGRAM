# Arithmetic Operations
a = 10
b = 3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print("Arithmetic Operations:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
print()

# Logical Operations
x = True
y = False
logical_and = x and y
logical_or = x or y
logical_not = not x

print("Logical Operations:")
print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")
print(f"Logical NOT: {logical_not}")
print()

# Assignment Operations
num = 10
num += 5  # equivalent to num = num + 5
print("Assignment Operations:")
print(f"num after addition assignment: {num}")
print()

# Comparison Operations
p = 5
q = 7
print("Comparison Operations:")
print(f"p == q: {p == q}")
print(f"p != q: {p != q}")
print(f"p > q: {p > q}")
print(f"p < q: {p < q}")
print()

# Bitwise Operations
num1 = 10  # 1010 in binary
num2 = 7   # 0111 in binary
bitwise_and = num1 & num2
bitwise_or = num1 | num2
bitwise_xor = num1 ^ num2
bitwise_not = ~num1
left_shift = num1 << 1
right_shift = num1 >> 1

print("Bitwise Operations:")
print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT: {bitwise_not}")
print(f"Left Shift: {left_shift}")
print(f"Right Shift: {right_shift}")
print()

# Membership Operations
list1 = [1, 2, 3, 4]
print("Membership Operations:")
print(f"2 in list1: {2 in list1}")
print(f"5 not in list1: {5 not in list1}")
print()

# Identity Operations
a = [1, 2, 3]
b = [1, 2, 3]
print("Identity Operations:")
print(f"a is b: {a is b}")
print(f"a is not b: {a is not b}")
