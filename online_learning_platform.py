# online_learning_platform.py

class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(self.username, "has logged in.")


class Student(User):

    def __init__(self, username, email):
        User.__init__(self, username, email)

    def enroll_course(self, course):
        print(self.username, "enrolled in", course)

    def view_grades(self):
        print(self.username, "is viewing grades.")


class Instructor(User):

    def __init__(self, username, email):
        User.__init__(self, username, email)

    def create_course(self, course):
        print(self.username, "created", course)

    def grade_assignment(self):
        print(self.username, "graded assignments.")


class StudentInstructor(Student, Instructor):

    def __init__(self, username, email):

        Student.__init__(self, username, email)

    def display_role(self):
        print(self.username,
              "acts as both Student and Instructor.")


student1 = Student(
    "john",
    "john@gmail.com"
)

instructor1 = Instructor(
    "sarah",
    "sarah@gmail.com"
)

user1 = StudentInstructor(
    "peter",
    "peter@gmail.com"
)

print("\nSTUDENT")
student1.login()
student1.enroll_course("Python Programming")
student1.view_grades()

print("\nINSTRUCTOR")
instructor1.login()
instructor1.create_course("Database Systems")
instructor1.grade_assignment()

print("\nSTUDENT INSTRUCTOR")
user1.login()
user1.enroll_course("Software Engineering")
user1.create_course("Web Development")
user1.display_role()

print("\nMRO")
print(StudentInstructor.mro())