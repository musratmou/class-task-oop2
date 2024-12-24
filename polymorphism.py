class Department:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Department Name: {self.name}")

class Teacher(Department):
    def __init__(self, name):
        super().__init__(name)

    def schedule_class(self):
        print("Class has been scheduled.")

    def grade_student(self):
        print("Student has been graded.")

    def display_name(self):
        super().display_name()
        print("This is a teacher.")

class TeacherAuthor(Teacher):
    def write_article(self):
        print("Article has been written.")

    def publish_blog(self):
        print("Blog has been published.")

teacher_author = TeacherAuthor("Computer Science")
teacher_author.display_name()
teacher_author.schedule_class()
teacher_author.grade_student()
teacher_author.write_article()
teacher_author.publish_blog()

