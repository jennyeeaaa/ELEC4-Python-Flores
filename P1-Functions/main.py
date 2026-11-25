def get_grades():
    grades = []

    num = int(input("How many grades will you enter? "))

    for i in range(num):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade! Enter a grade from 0 to 100.")

            except ValueError:
                print("Please enter a valid number.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def check_result(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def display_results(grades):
    average = calculate_average(grades)

    print("\n===== STUDENT GRADE RESULTS =====")
    print("Grades:", grades)
    print("Average:", round(average, 2))
    print("Highest Grade:", get_highest(grades))
    print("Lowest Grade:", get_lowest(grades))
    print("Status:", check_result(average))


def display_menu():
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("1. Calculate Average")
    print("2. Display Highest Grade")
    print("3. Display Lowest Grade")
    print("4. Check Pass or Fail")
    print("5. Display All Results")
    print("0. Exit")


def main():
    grades = get_grades()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Average:", round(calculate_average(grades), 2))

        elif choice == "2":
            print("Highest Grade:", get_highest(grades))

        elif choice == "3":
            print("Lowest Grade:", get_lowest(grades))

        elif choice == "4":
            average = calculate_average(grades)
            print("Status:", check_result(average))

        elif choice == "5":
            display_results(grades)

        elif choice == "0":
            print("Thank you for using the Student Grade Calculator!")
            break

        else:
            print("Invalid choice! Please select from 0 to 5.")


if __name__ == "__main__":
    main()