# Inportant: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty ser can be created using the below syntax
b = set()
print(type(b))
b.add(4) # add 4 to the set
b.add(5)
print(b)