"""
Jenny Flores
IV-BSIT C
ELEC 4 - P5 Student Information File System
"""

FILE_NAME = "students.txt"


def load_records():
    records = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    student = {
                        "id": data[0],
                        "name": data[1],
                        "course": data[2],
                        "average": data[3]
                    }
                    records.append(student)

    except FileNotFoundError:
        print("No existing student file found. Starting with an empty list.")

    return records


def save_records(records):
    with open(FILE_NAME, "w") as file:
        for student in records:
            file.write(
                f"{student['id']}|{student['name']}|"
                f"{student['course']}|{student['average']}\n"
            )


def add_student(records):
    print("\n--- ADD STUDENT ---")

    student_id = input("Enter Student ID: ").strip()

    if any(student["id"] == student_id for student in records):
        print("Student ID already exists!")
        return

    name = input("Enter Full Name: ").strip()
    course = input("Enter Course/Section: ").strip()

    try:
        average = float(input("Enter General Average: "))

        if not 0 <= average <= 100:
            print("Average must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid input! Please enter a number for the average.")
        return

    if not student_id or not name or not course:
        print("All fields are required.")
        return

    records.append({
        "id": student_id,
        "name": name,
        "course": course,
        "average": str(average)
    })

    save_records(records)
    print("Student record added successfully!")


def display_students(records):
    print("\n--- ALL STUDENT RECORDS ---")

    if not records:
        print("No student records found.")
        return

    for student in records:
        print("--------------------------------")
        print("Student ID:", student["id"])
        print("Full Name:", student["name"])
        print("Course/Section:", student["course"])
        print("General Average:", student["average"])


def search_student(records):
    print("\n--- SEARCH STUDENT ---")

    student_id = input("Enter Student ID to search: ").strip()

    for student in records:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Full Name:", student["name"])
            print("Course/Section:", student["course"])
            print("General Average:", student["average"])
            return

    print("Student not found.")


def update_student(records):
    print("\n--- UPDATE STUDENT ---")

    student_id = input("Enter Student ID to update: ").strip()

    for student in records:
        if student["id"] == student_id:
            print("Leave a field blank to keep its current value.")

            name = input(f"Enter new name ({student['name']}): ").strip()
            course = input(f"Enter new course/section ({student['course']}): ").strip()
            average = input(f"Enter new average ({student['average']}): ").strip()

            if average:
                try:
                    new_average = float(average)

                    if not 0 <= new_average <= 100:
                        print("Average must be between 0 and 100.")
                        return

                    student["average"] = str(new_average)

                except ValueError:
                    print("Invalid input! Average must be a number.")
                    return

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            save_records(records)
            print("Student record updated successfully!")
            return

    print("Student not found.")


def main():
    records = load_records()

    while True:
        print("\n================================")
        print(" STUDENT INFORMATION FILE SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Information")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            display_students(records)
        elif choice == "3":
            search_student(records)
        elif choice == "4":
            update_student(records)
        elif choice == "5":
            print("Thank you for using the Student Information File System!")
            break
        else:
            print("Invalid choice! Please select from 1 to 5.")


if _name_ == "_main_":
    main()
9:29 AM
You sent
P5 – Student Information File System

Name: Jenny Flores
Section: IV-BSIT C
Subject: ELEC 4

Description

A Python program that manages student information using text file handling. It allows users to add, display, search, and update student records.

Features

* Add student records
* Display all student records
* Search students by ID
* Update student information
* Save and load records using students.txt
* Handle missing files and invalid inputs

How to Run

1. Open the terminal.
2. Navigate to the P5-File-System folder.
3. Run:

py p5_file_system.py

Files

* p5_file_system.py – Main Python program
* students.txt – Stores student records