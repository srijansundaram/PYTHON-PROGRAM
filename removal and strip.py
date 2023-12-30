def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "             Srijan is bad            "
n = remove_and_split(this, "Srijan")
print(n)

# strip removes extra spaces.