with open ("log.txt") as f:
    content = f.read().lower() # . lower will lowercase every charcter in the file

if 'python' in content: # we can use . lower over here as well. Here it lower charcter menioned in the condition
    print("Yes python is present")
else:
    print("No python is not present")
