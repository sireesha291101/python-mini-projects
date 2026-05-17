students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students.append((name, marks))
    print("Student Added!")

def show_students():
    print("\n--- Student List ---")

    for student in students:
        print(student[0], "-", student[1])

def average_marks():
    total = 0

    for student in students:
        total += student[1]

    avg = total / len(students)
    print("Average Marks =", avg)


def highest_marks():

    highest = max(student[1] for student in students)

    print("\nTopper(s):")

    for student in students:
        if student[1] == highest:
            print(student[0], "-", student[1])

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Average Marks")
    print("4. Highest Marks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        average_marks()

    elif choice == "4":
        highest_marks()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")