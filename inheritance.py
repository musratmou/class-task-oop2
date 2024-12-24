class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}")


class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print(f"Graduation Year: {self.graduation_year}")


class Teacher(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")


class Admin(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")


class Alumni(Student):
    def __init__(self, first_name, last_name, graduation_year, passing_year):
        super().__init__(first_name, last_name, graduation_year)
        self.passing_year = passing_year

    def display(self):
        super().display()
        print(f"Passing Year: {self.passing_year}")


class CurrentStudent(Student):
    def __init__(self, first_name, last_name, graduation_year, current_semester):
        super().__init__(first_name, last_name, graduation_year)
        self.current_semester = current_semester

    def display(self):
        super().display()
        print(f"Current Semester: {self.current_semester}")


class Employee(Admin, Teacher):
    def __init__(self, first_name, last_name, joining_year, emp_id):
        Admin.__init__(self, first_name, last_name, joining_year)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")


student = Student("John", "Doe", 2025)
teacher = Teacher("Jane", "Smith", 2015)
admin = Admin("Alice", "Johnson", 2010)
alumni = Alumni("Mike", "Brown", 2020, 2021)
current_student = CurrentStudent("Emma", "Davis", 2026, "5th")
employee = Employee("Robert", "Taylor", 2018, "E123")

print("Student Details:")
student.display()
print("\nTeacher Details:")
teacher.display()
print("\nAdmin Details:")
admin.display()
print("\nAlumni Details:")
alumni.display()
print("\nCurrent Student Details:")
current_student.display()
print("\nEmployee Details:")
employee.display()
