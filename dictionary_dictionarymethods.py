myDict = {
    "Fast": "In a Quick Manner",
    "Python": "Programming Language",
    "Marks": [1, 2, 5],
    "anotherdict": {"Python": "Easy and Simple"},
    1: 2  # 1 is also a key which stores 2 as its value
}
 
# print(myDict.keys()) # this will print the keys of myDict which is fast, python, etc.
# print(type(myDict.keys())) # this will check the data type
# print(list(myDict.keys())) # this will convert it into list data type
# print(myDict.values()) # this will print the value of the keys
# print(myDict.items()) # print the (key, value) for all contents of the dictionary
# print(myDict)
# updateDict = {
#     "Lovish": "Friend",
#     "Python": "Object oriented language" # update the value of python
# }
# myDict.update(updateDict) # updates the dictionary by adding key-value pairs from updatedict
# print(myDict)
# print(myDict.get("Python")) # prints value associated with 'Python'
# print(myDict["Python"]) # prints value associated with 'Python'
# Difference is if a key is not present in string 'get' will return none whereas '[]' throws an error
