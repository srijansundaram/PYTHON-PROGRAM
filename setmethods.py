# An empty ser can be created using the below syntax

# b = set()
# print(type(b))

# adding element to the set

# b.add(4) # add 4 to the set
# b.add(5)

#  we cannot add list, dictionary in the set. But tuple can be added
# b.add((4, 5, 6)) # adding tuple to the set
# print(b)

# removing element from the set:
# b.remove(5) # removes 5 from the set
# print(b)

# removes a random element from the set and returns the removed element
# print(b.pop())

# empties the set
# print(b.clear())

# reaturn a new set wih all items from the both sets. That is union of the sets
# print(b.union({8,11}))

# returns a set which contaily only items in both sets. That is intersection.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)