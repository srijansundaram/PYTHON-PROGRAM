m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

if(m1<33 or m2<33 or m3<33):
    print("You are fail as you score less than 33% in any one subject.\n")
elif((m1+m2+m3)/3 < 40):
    print("You are fail as your total percentage is less than 40.\n")
else:
    print("Congratulations! You are passed.\n")
    