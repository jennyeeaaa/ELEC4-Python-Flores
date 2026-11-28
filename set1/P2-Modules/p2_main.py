import student_utils
from student_utils import calculate_average
from datetime import datetime


def main():
    grades = []

    print("===== STUDENT GRADE REPORT =====")

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

    average = calculate_average(grades)

    print("\n===== GRADE RESULTS =====")
    print("Grades:", grades)
    print("Average:", round(average, 2))
    print("Highest Grade:", student_utils.get_highest(grades))
    print("Lowest Grade:", student_utils.get_lowest(grades))
    print("Status:", student_utils.check_result(average))
    print("Report Generated:", datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))


if __name__ == "__main__":
    main()