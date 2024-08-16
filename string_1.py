# Creating Strings
string1 = "Hello"
string2 = "World"
string3 = "Python Programming"

# Concatenating Strings
concatenated_string = string1 + " " + string2 + "! Welcome to " + string3 + "."

# Printing the Concatenated String
print("Concatenated String:")
print(concatenated_string)

# Accessing Substrings
# Extracting "World" from the concatenated string
substring1 = concatenated_string[6:11]  # Starts at index 6, ends at index 11 (exclusive)

# Extracting "Programming" from string3
substring2 = string3[7:]  # Starts at index 7 to the end

# Printing Substrings
print("\nExtracted Substrings:")
print("Substring 1:", substring1)
print("Substring 2:", substring2)
