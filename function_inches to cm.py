def len_convert(centi):
    return centi / 2.54

len = int(input("Enter length in centimetre: "))
print(len, "centimetre is", len_convert(len), "inches")