numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate even and odd numbers into two different lists
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Merge and sort the two lists
merged_list = sorted(even_numbers + odd_numbers)
print("Merged and sorted list:", merged_list)

# Update the first element with X value
merged_list[0] = '41'
print("Updated list:", merged_list)

# Delete the middle element of the list
middle_index = len(merged_list) // 2
del merged_list[middle_index]
print("List after deleting middle element:", merged_list)

# Find max and min elements from the list
max_element = max(merged_list[1:])  # excluding '41'
min_element = min(merged_list[1:])  # excluding '41'
print("Max element:", max_element)
print("Min element:", min_element)

# Add N names into the existing number list
names = ["John", "Alice", "Bob", "Python"]
merged_list.extend(names)
print("List after adding names:", merged_list)

# Check if word python is present in the list
if "Python" in merged_list:
    print("Word 'Python' is present in the list.")
else:
    print("Word 'Python' is not present in the list.")