
"""
Jenny Flores
IV-BSIT C
ELEC 4 - P8 Inheritance and Polymorphism
"""


# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")


# Child Class 1
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    # Method Overriding
    def introduce(self):
        print("\n--- STUDENT INTRODUCTION ---")
        print(f"Hi! I am {self.name}, {self.age} years old.")
        print(f"My Student ID is {self.student_id}.")
        print(f"I am taking {self.course}.")


# Child Class 2
class Teacher(Person):
    def __init__(self, name, age, subject, employee_id):
        super().__init__(name, age)
        self.subject = subject
        self.employee_id = employee_id

    # Method Overriding
    def introduce(self):
        print("\n--- TEACHER INTRODUCTION ---")
        print(f"Good day! I am Teacher {self.name}, {self.age} years old.")
        print(f"My Employee ID is {self.employee_id}.")
        print(f"I teach {self.subject}.")


# Main Program
def main():
    # Create objects from different classes
    person1 = Person("Alex Cruz", 30)
    student1 = Student("Jenny Flores", 21, "2026-001", "BS Information Technology")
    student2 = Student("Maria Santos", 22, "2026-002", "BS Information Technology")
    teacher1 = Teacher("Mr. Reyes", 35, "Python Programming", "T-101")

    # Store different objects in one list
    people = [person1, student1, student2, teacher1]

    # Demonstrate polymorphism
    print("================================")
    print("   INHERITANCE AND POLYMORPHISM")
    print("================================")

    for person in people:
        person.introduce()


if __name__ == "__main__":
    main()


# Explanation:
# Inheritance is demonstrated because Student and Teacher inherit
# the common attributes and methods from the Person parent class.
# The super().__init__() method initializes the name and age attributes.
# Polymorphism is shown when different objects are placed in one list
# and the same introduce() method produces different outputs.

