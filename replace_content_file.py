with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("sample.txt", "w") as f:
    f.write(content)

#  For multiple words in a list:
#     words = ["donkey", 'kaddu', 'mote']

#     with open("sample.txt") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "$%^@$^#")
#     with open("sample.txt", "w") as f:
#         f.write(content)