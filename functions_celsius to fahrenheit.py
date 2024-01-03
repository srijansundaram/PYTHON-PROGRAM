def temp_convert(cel):
    return (cel * (9/5)) + 32

temp = int(input("Enter temperature in celsius: "))
print(temp, "degree celsius in fahrenheit is", temp_convert(temp))