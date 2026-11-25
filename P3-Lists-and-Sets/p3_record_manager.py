students = []
student_set = set()


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name.casefold() in student_set:
        print("Student already exists!")
    else:
        students.append(name)
        student_set.add(name.casefold())
        print(f"{name} has been added successfully!")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.casefold() == name.casefold():
            students.remove(student)
            student_set.remove(student.casefold())
            print(f"{student} has been removed successfully!")
            return

    print("Student not found!")


def search_student():
    name = input("Enter name to search: ").strip().casefold()

    if not name:
        print("Please enter a name to search.")
        return

    found = [student for student in students
             if name in student.casefold()]

    if found:
        print("\nSearch Results:")
        for student in found:
            print("-", student)
    else:
        print("No matching student found!")


def display_students():
    print("\n===== STUDENT RECORDS =====")

    if not students:
        print("No students in the record.")
    else:
        for number, student in enumerate(sorted(students, key=str.casefold), start=1):
            print(f"{number}. {student}")

    print("Total Students:", len(students))


def display_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("0. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "0":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice! Please select from 0 to 4.")


if __name__ == "__main__":
    main()


# Difference between a list and a set:
# A list stores items in order and allows duplicate values.
# A set stores only unique values and is useful for checking duplicates.
# In this program, the students list stores the student names.
# The student_set checks if a name already exists, ignoring uppercase
# and lowercase differences.