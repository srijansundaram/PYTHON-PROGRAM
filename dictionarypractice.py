myDict = {
    "paani": "Water",
    "gaadi": "vehicle",
    "bistar": "bed",
    "pankha": "Fan"
}
print("Options are: ", myDict.keys())
a = input("Enter the Hindi Word whose meaning you want\n")
print("The meaning of your word is: ", myDict.get(a))