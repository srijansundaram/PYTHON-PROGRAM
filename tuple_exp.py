# Initialize an empty list to store student information
students = []

def add_student():
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        roll_number = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks1 = float(input("Enter mark 1: "))
        marks2 = float(input("Enter mark 2: "))
        marks3 = float(input("Enter mark 3: "))
        student = (roll_number, name, marks1, marks2, marks3)
        students.append(student)

def show_students():
    for student in students:
        print(student)

def find_python_students():
    python_students = [student for student in students if student[1] == 'Python']
    for student in python_students:
        print(f"Roll Number: {student[0]}, Marks: {student[2:]}")


def nested_tuple_demo():
    nested_tuple = (('John', 20), ('Alice', 22), ('Bob', 21), ('Python', 25))
    print("Original Nested Tuple:")
    print(nested_tuple)
    sorted_nested_tuple = sorted(nested_tuple, key=lambda x: x[0])
    print("Sorted Nested Tuple by Name:")
    print(sorted_nested_tuple)


def main():
    while True:
        print("\nMenu:")
        print("1. Add students")
        print("2. Show students")
        print("3. Find Python students")
        print("4. Nested tuple demo")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            show_students()
        elif choice == 3:
            find_python_students()
        elif choice == 4:
            nested_tuple_demo()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()