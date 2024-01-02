f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present.\n")
else:
     print("Twinkle is not present.\n")
f.close()