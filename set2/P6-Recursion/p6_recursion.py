
"""
Jenny Flores
IV-BSIT C
ELEC 4 - P6 Recursion Toolkit
"""


# Base case: If n is 0 or 1, return 1.
# Recursive call: Multiply n by factorial of n - 1.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Base case: If n is 0, return 0; if n is 1, return 1.
# Recursive call: Add the previous two Fibonacci numbers.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: If n is 0, return 0.
# Recursive call: Add n to the sum of numbers from 1 to n - 1.
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case: If the list is empty, the target is not found.
# Recursive call: Search the remaining list one item at a time.
def search(items, target):
    if len(items) == 0:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def main():
    while True:
        print("\n==============================")
        print("       RECURSION TOOLKIT")
        print("==============================")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of Numbers")
        print("4. Search in a List")
        print("5. Exit")

        choice = input("Choose a function (1-5): ").strip()

        if choice == "1":
            try:
                n = int(input("Enter a non-negative number: "))
                if n < 0:
                    print("Please enter a non-negative number.")
                else:
                    print("Factorial:", factorial(n))
            except ValueError:
                print("Invalid input! Please enter a whole number.")

        elif choice == "2":
            try:
                n = int(input("Enter the number of terms: "))
                if n <= 0:
                    print("Please enter a number greater than 0.")
                else:
                    terms = [fibonacci(i) for i in range(n)]
                    print("Fibonacci sequence:", terms)
                    print("Nth Fibonacci number:", fibonacci(n - 1))
            except ValueError:
                print("Invalid input! Please enter a whole number.")

        elif choice == "3":
            try:
                n = int(input("Enter a positive number: "))
                if n < 0:
                    print("Please enter a non-negative number.")
                else:
                    print("Sum:", sum_numbers(n))
            except ValueError:
                print("Invalid input! Please enter a whole number.")

        elif choice == "4":
            items = input("Enter list items separated by spaces: ").split()
            target = input("Enter the value to search: ")
            print("Found:", search(items, target))

        elif choice == "5":
            print("Thank you for using the Recursion Toolkit!")
            break

        else:
            print("Invalid choice! Please select from 1 to 5.")


if __name__ == "__main__":
    main()
