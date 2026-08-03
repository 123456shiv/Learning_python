print("Welcome to the Student Menu!")
print("1. View name")
print("2. View grades")
print("3. View attendance")
print("4. Exit")

studentnumber = int(input("Enter your student number: "))
match studentnumber:
    case 1: 
        name=input("Enter your name: ")
        print("Student Name: ", name)

    case 2:
        grades=int(input("Enter your grades: "))
        print("Student Grades: ", grades)

    case 3:
        attendance=int(input("Enter your attendance: "))
        print("Student Attendance: ", attendance)

    case 4:
        print("Thank you for using the Student Menu!")

    case _:
        print("Invalid student number. Please try again.")