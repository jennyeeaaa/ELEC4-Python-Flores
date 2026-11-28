
"""
Jenny Flores
IV-BSIT C
ELEC 4 - P7 Student Management System with Classes
"""


# Class 1: Student
class Student:
    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__grade = 0
        self.set_grade(grade)

    # Display student information
    def display_info(self):
        print("------------------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Grade:", self.get_grade())

    # Read private grade
    def get_grade(self):
        return self.__grade

    # Update private grade with validation
    def set_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.__grade = grade
            return True
        else:
            print("Invalid grade! Grade must be between 0 and 100.")
            return False

    # Update student information
    def update_info(self, name, course):
        self.name = name
        self.course = course
        print("Student information updated successfully!")


# Class 2: Subject
class Subject:
    def __init__(self, subject_name, subject_code):
        self.subject_name = subject_name
        self.subject_code = subject_code

    def display_subject(self):
        print("Subject:", self.subject_name)
        print("Subject Code:", self.subject_code)


# Class 3: Section
class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_section(self):
        print("\n================================")
        print("       STUDENT MANAGEMENT")
        print("================================")
        print("Section:", self.section_name)
        self.subject.display_subject()

        print("\nSTUDENT LIST")
        for student in self.students:
            student.display_info()


# Main Program
def main():
    # Create a subject object
    subject = Subject("Object-Oriented Programming", "ELEC4")

    # Create a section object
    section = Section("IV-BSIT C", subject)

    # Create three student objects
    student1 = Student("2026-001", "Jenny Flores", "BSIT", 92)
    student2 = Student("2026-002", "Maria Santos", "BSIT", 89)
    student3 = Student("2026-003", "John Reyes", "BSIT", 91)

    # Add students to the section
    section.add_student(student1)
    section.add_student(student2)
    section.add_student(student3)

    # Update one student's information
    print("\n--- UPDATE STUDENT ---")
    student2.update_info("Maria Santos Updated", "BSIT - IV-BSIT C")
    student2.set_grade(95)

    # Demonstrate grade validation
    print("\n--- GRADE VALIDATION ---")
    student2.set_grade(105)

    # Display all students
    section.display_section()


if __name__ == "__main__":
    main()
