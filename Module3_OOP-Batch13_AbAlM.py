# =========================================================
#   STUDENT MANAGEMENT SYSTEM
# =========================================================

class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.department = department
        self.__email = email          # Encapsulation (private)
        self.__marks = []             # Encapsulation (private)

    # --- Encapsulation: controlled access ---
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def add_marks(self, *marks):      # Method Overloading (*args)
        self.__marks.extend(marks)

    # --- Common methods ---
    def display_info(self, show_marks=False):   # Overloading (default arg)
        print(f"Name       : {self.name}")
        print(f"ID         : {self.student_id}")
        print(f"Email      : {self.__email}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")
        if show_marks:
            print(f"Marks      : {self.__marks}")

    def calculate_result(self):
        if not self.__marks:
            return 0
        return sum(self.__marks) / len(self.__marks)

    def get_student_type(self):
        return "Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester                 # New attribute

    def get_student_type(self):                  # Override
        return "Undergraduate Student"

    def calculate_result(self):                  # Override
        avg = super().calculate_result()
        return f"Average = {avg:.2f} | {'PASS' if avg >= 40 else 'FAIL'}"


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic     # New attribute

    def get_student_type(self):                  # Override
        return "Graduate Student"

    def calculate_result(self):                  # Override
        avg = super().calculate_result()
        return f"Average = {avg:.2f} | {'PASS' if avg >= 60 else 'FAIL'}"


# =========================================================
#                    DEMONSTRATION
# =========================================================
ug = UndergraduateStudent("Yamin", "UG101", "yamin@uni.edu", 20, "CSE", 5)
grad = GraduateStudent("Imon", "GR201", "imon@uni.edu", 26, "CSE", "Machine Learning")

ug.add_marks(78, 85, 90)
grad.add_marks(55, 72, 68, 80)

for s in [ug, grad]:                              # Polymorphism
    print("=" * 45)
    s.display_info(show_marks=True)
    print("Type   :", s.get_student_type())
    print("Result :", s.calculate_result())
    print("=" * 45)