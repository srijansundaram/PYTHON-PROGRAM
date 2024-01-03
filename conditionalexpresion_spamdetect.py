comment = input("Enter your comment: ")
if("Make a lot of money" in comment or "make a lot of money" in comment):
    spam = True
elif("Buy now" in comment or "buy now" in comment):
    spam = True
elif("Subscribe this" in comment or "subscribe this" in comment):
    spam = True
elif("Click this" in comment or "click this" in comment):
    spam = True
else:
    spam = False

if(spam):
    print("This comment is spam.\n")
else:
    print("This text is not spam.\n")