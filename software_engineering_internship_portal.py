# software_engineering_internship_portal.py

class User:

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def login(self):
        print(self.name, "has logged in.")

    def logout(self):
        print(self.name, "has logged out.")

    def display_profile(self):
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Email:", self.email)


class Student(User):

    def __init__(self,
                 user_id,
                 name,
                 email,
                 registration_number,
                 course):

        User.__init__(
            self,
            user_id,
            name,
            email
        )

        self.registration_number = registration_number
        self.course = course

    def display_profile(self):

        User.display_profile(self)

        print("Registration Number:",
              self.registration_number)

        print("Course:",
              self.course)


class Supervisor(User):

    def __init__(self,
                 user_id,
                 name,
                 email,
                 company_name,
                 employee_id):

        User.__init__(
            self,
            user_id,
            name,
            email
        )

        self.company_name = company_name
        self.employee_id = employee_id

    def display_profile(self):

        User.display_profile(self)

        print("Company Name:",
              self.company_name)

        print("Employee ID:",
              self.employee_id)


class StudentRepresentative(Student):

    def __init__(self,
                 user_id,
                 name,
                 email,
                 registration_number,
                 course,
                 company_name,
                 employee_id):

        Student.__init__(
            self,
            user_id,
            name,
            email,
            registration_number,
            course
        )

        self.company_name = company_name
        self.employee_id = employee_id

    # Method overriding
    def display_profile(self):

        print("\nSTUDENT REPRESENTATIVE PROFILE")

        User.display_profile(self)

        print("Registration Number:",
              self.registration_number)

        print("Course:",
              self.course)

        print("Company Name:",
              self.company_name)

        print("Employee ID:",
              self.employee_id)


# Creating Objects

student1 = Student(
    "U001",
    "John",
    "john@gmail.com",
    "REG001",
    "Information Technology"
)

supervisor1 = Supervisor(
    "U002",
    "Sarah",
    "sarah@gmail.com",
    "Tech Solutions Ltd",
    "EMP001"
)

rep1 = StudentRepresentative(
    "U003",
    "Peter",
    "peter@gmail.com",
    "REG002",
    "Software Engineering",
    "Future Systems Ltd",
    "EMP002"
)

print("\nSTUDENT")
student1.login()
student1.display_profile()
student1.logout()

print("\nSUPERVISOR")
supervisor1.login()
supervisor1.display_profile()
supervisor1.logout()

print("\nSTUDENT REPRESENTATIVE")
rep1.login()
rep1.display_profile()
rep1.logout()

print("\nMETHOD RESOLUTION ORDER")
print(StudentRepresentative.mro())