# university_management_system.py

class Person:

    def __init__(self, name, national_id, email):
        self.name = name
        self.national_id = national_id
        self.email = email

    def display_person(self):
        print("Name:", self.name)
        print("National ID:", self.national_id)
        print("Email:", self.email)


class Student(Person):

    def __init__(self, name, national_id, email,
                 registration_number, program):

        Person.__init__(self, name, national_id, email)

        self.registration_number = registration_number
        self.program = program

    def display_student(self):

        self.display_person()

        print("Registration Number:", self.registration_number)
        print("Program:", self.program)


class Staff(Person):

    def __init__(self, name, national_id, email,
                 employee_number, department):

        Person.__init__(self, name, national_id, email)

        self.employee_number = employee_number
        self.department = department

    def display_staff(self):

        self.display_person()

        print("Employee Number:", self.employee_number)
        print("Department:", self.department)


class TeachingAssistant(Student):

    def __init__(self,
                 name,
                 national_id,
                 email,
                 registration_number,
                 program,
                 employee_number,
                 department):

        Student.__init__(
            self,
            name,
            national_id,
            email,
            registration_number,
            program
        )

        self.employee_number = employee_number
        self.department = department

    def display_ta(self):

        self.display_student()

        print("Employee Number:", self.employee_number)
        print("Department:", self.department)


# Creating objects

student1 = Student(
    "John",
    "CM12345",
    "john@gmail.com",
    "REG001",
    "Information Technology"
)

staff1 = Staff(
    "Sarah",
    "CM67890",
    "sarah@gmail.com",
    "EMP001",
    "Computer Science"
)

ta1 = TeachingAssistant(
    "Peter",
    "CM11111",
    "peter@gmail.com",
    "REG002",
    "Software Engineering",
    "EMP002",
    "ICT Support"
)

print("\nSTUDENT DETAILS")
student1.display_student()

print("\nSTAFF DETAILS")
staff1.display_staff()

print("\nTEACHING ASSISTANT DETAILS")
ta1.display_ta()

print("\nMRO")
print(TeachingAssistant.mro())