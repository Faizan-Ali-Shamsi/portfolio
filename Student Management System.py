import os

# Where to store student records
FILE_NAME = "students.txt"

# Main Menu


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by Roll No")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.\n")

# Function to add a new student


def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter name: ")
    try:
        m1 = int(input("Enter marks for subject 1: "))
        m2 = int(input("Enter marks for subject 2: "))
        m3 = int(input("Enter marks for subject 3: "))
    except ValueError:
        print("Invalid input! Marks should be integers.\n")
        return

    # Prevent duplicate roll numbers
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                r, *_ = line.strip().split(",")
                if r == roll_no:
                    print("Error: Roll number already exists!\n")
                    return

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll_no},{name},{m1},{m2},{m3}\n")
    print("Student added successfully!\n")

# Function to view all students


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    print("\n===== Student Records =====")
    with open(FILE_NAME, "r") as f:
        for line in f:
            roll_no, name, m1, m2, m3 = line.strip().split(",")
            marks = [int(m1), int(m2), int(m3)]
            avg = sum(marks) / 3
            grade = calculate_grade(avg)
            print(
                f"Roll No: {roll_no}, Name: {name}, Marks: {marks}, Average: {avg:.2f}, Grade: {grade}"
            )
    print()
    input("Press Enter to continue...")

# Function to search student by roll number


def search_student():
    roll_no = input("Enter roll number to search: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            r, name, m1, m2, m3 = line.strip().split(",")
            if r == roll_no:
                marks = [int(m1), int(m2), int(m3)]
                avg = sum(marks) / 3
                grade = calculate_grade(avg)
                print(
                    f"Roll No: {r}, Name: {name}, Marks: {marks}, Average: {avg:.2f}, Grade: {grade}\n"
                )
                found = True
                break

    if not found:
        print("Student not found.\n")

    input("Press Enter to continue...")

# Function to calculate grade based on average marks


def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


if __name__ == "__main__":
    main()
