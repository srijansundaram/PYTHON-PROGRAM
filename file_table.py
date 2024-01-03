num = int(input("Enter a number: "))

with open(f"Multiplication_table.txt") as f:
    table = (f.read())

if table == '':
    with open(f"Multiplication_table.txt","w") as f:
        f.write(f"Multiplication_table_of_{num}\n")
        for j in range(1, 11):
            f.write(f"{num} x {j} = {num*j}")
            if j != 10:
                f.write("\n")

elif 'Multiplication_table_of_' in table:
        with open(f"Multiplication_table.txt","w") as f:
            f.write(f"Multiplication_table_of_{num}\n")
            for j in range(1, 11):
                f.write(f"{num} x {j} = {num*j}")
                if j != 10:
                    f.write("\n")