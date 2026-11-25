def divide_numbers():
    print("\n===== DIVISION CALCULATOR =====")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    except ZeroDivisionError:
        print("Error! Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")


def open_file():
    print("\n===== OPEN FILE =====")

    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error! File not found.")

    else:
        print("\nFile Contents:")
        print(content)

    finally:
        print("File operation completed.")


def display_menu():
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Divide Numbers")
    print("2. Open a File")
    print("0. Exit")


def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Invalid menu input! Please enter a number.")
            continue

        if choice == 1:
            divide_numbers()

        elif choice == 2:
            open_file()

        elif choice == 0:
            print("Thank you for using Safe Menu Program!")
            break

        else:
            print("Invalid menu selection! Please choose 0, 1, or 2.")


if __name__ == "__main__":
    main()
