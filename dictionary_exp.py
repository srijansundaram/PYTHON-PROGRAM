# Create a dictionary with key/value pairs
my_dict = {"name": "John", "age": 30, "city": "New York"}

print("Original Dictionary:")
print(my_dict)

# Update an existing item in the dictionary
my_dict["age"] = 31
print("\nUpdated Dictionary:")
print(my_dict)

# Concatenate a new item to the dictionary
my_dict["country"] = "USA"
print("\nUpdated Dictionary after concatenation:")
print(my_dict)

# Delete an item from the dictionary
del my_dict["city"]
print("\nUpdated Dictionary after deletion:")
print(my_dict)

# Find a key and print its value
key_to_find = "name"
if key_to_find in my_dict:
    print(f"\nThe value of '{key_to_find}' is: {my_dict[key_to_find]}")
else:
    print(f"The key '{key_to_find}' does not exist in the dictionary.")
