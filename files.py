#  Use open function to read the content of a file.

# f = open('sample.txt', 'r')
f = open('sample.txt') # by default the node is r.

data = f.read()
# data = f.read(5) # reads first 5 characters of the file

print(data)
f.close()

# f.readline() will print one line at a time.
# 'rb' means read in binary mode.
# 'rt' means read in text mode. By default it is in text mode.
 