"""
Name: Benz Josue
Program: Gradebook System
Description: This program implements a simple gradebook system for CSC/DSCI 1301.
It allows adding students, grade items, student grades, and printing individual and class grades.
"""

# Custom Exceptions
class EmptyRosterError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class GradeItemNotFoundError(Exception):
    pass

# Student Class
class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

# GradeItem Class
class GradeItem:
    def __init__(self, name, total_points):
        self.name = name
        self.total_points = total_points
        self.grades = {}

    def add_student_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_name(self):
        return self.name

    def get_total_points(self):
        return self.total_points

    def get_student_grade(self, student_id):
        if student_id in self.grades:
            return self.grades[student_id]
        else:
            return "N/A"

# Course Class
class Course:
    def __init__(self):
        self.roster = []
        self.grade_items = []

    def add_student(self, student):
        self.roster.append(student)

    def add_grade_item(self, grade_item):
        self.grade_items.append(grade_item)

    def find_student(self, student_id):
        for student in self.roster:
            if student.get_student_id() == student_id:
                return student
        return None

    def find_grade_item(self, item_name):
        for item in self.grade_items:
            if item.get_name() == item_name:
                return item
        return None

    def add_student_grade(self, item_name, student_id, grade):
        if len(self.roster) == 0:
            raise EmptyRosterError("Error: Course Roster is Empty!")

        student = self.find_student(student_id)
        if student is None:
            raise StudentNotFoundError(f"Exception: Student ({student_id}) not found.")

        item = self.find_grade_item(item_name)
        if item is None:
            raise GradeItemNotFoundError(f"Exception: Grade Item ({item_name}) not found.")

        item.add_student_grade(student_id, grade)

    def print_student_grades(self, student_id):
        student = self.find_student(student_id)
        if student is None:
            raise StudentNotFoundError(f"Exception: Student ({student_id}) not found.")

        print(f"{student.get_last_name()}, {student.get_first_name()} ({student_id})", end="")
        for item in self.grade_items:
            grade = item.get_student_grade(student_id)
            total = item.get_total_points()
            print(f" | {item.get_name()}: {grade} ({total})", end="")
        print()

    def print_roster(self):
        if len(self.roster) == 0:
            raise EmptyRosterError("Error: Course Roster is Empty!")
        print("Course Roster:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})")

    def print_class_grades(self):
        if len(self.roster) == 0:
            raise EmptyRosterError("Error: Course Roster is Empty!")
        print("Class Grades:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})", end="")
            for item in self.grade_items:
                grade = item.get_student_grade(student.get_student_id())
                total = item.get_total_points()
                print(f" | {item.get_name()}: {grade} ({total})", end="")
            print()

# Menu System
main_menu_running = True
course = Course()

print("Welcome to CSC/DSCI 1301: Principles in CS/DS 1")
while main_menu_running:
    print("""
Please choose one of the following options (Enter 'quit' or 'q' to exit).
1) Add a Student.
2) Add a Grade Item.
3) Add a Student's Grade.
4) Print a Student's Grades.
5) Print Course Roster
6) Print Class Grades.
""")
    choice = input(":> ")

    if choice.lower() in ['quit', 'q']:
        main_menu_running = False
        continue

    try:
        if choice == '1':
            first = input("Enter First Name: ")
            last = input("Enter Last Name: ")
            student_id_input = input("Enter Student ID: ")
            if not student_id_input.isdigit():
                print("Error: Enter a Integer Student ID")
                continue
            student_id = int(student_id_input)
            course.add_student(Student(first, last, student_id))

        elif choice == '2':
            name = input("Enter grade item name: ")
            points_input = input("Enter the total points for the grade item: ")
            if not points_input.isdigit():
                print("Error: Enter a Integer Grade Item Total Points")
                continue
            total_points = int(points_input)
            course.add_grade_item(GradeItem(name, total_points))

        elif choice == '3':
            item_name = input("Enter grade item name: ")
            student_id_input = input("Enter Student ID: ")
            grade_input = input("Enter Student Grade: ")
            if not (student_id_input.isdigit() and grade_input.isdigit()):
                print("Error: Enter a Integer Student ID or Grade")
                continue
            student_id = int(student_id_input)
            grade = int(grade_input)
            course.add_student_grade(item_name, student_id, grade)

        elif choice == '4':
            student_id_input = input("Enter Student ID: ")
            if not student_id_input.isdigit():
                print("Error: Enter a Integer Student ID")
                continue
            student_id = int(student_id_input)
            course.print_student_grades(student_id)

        elif choice == '5':
            course.print_roster()

        elif choice == '6':
            course.print_class_grades()

        else:
            print("Invalid choice.")

    except (EmptyRosterError, StudentNotFoundError, GradeItemNotFoundError) as e:
        print(e)


