# hospital_information_system.py

class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


class Patient(Person):

    def __init__(self,
                 name,
                 age,
                 gender,
                 patient_id,
                 disease):

        Person.__init__(
            self,
            name,
            age,
            gender
        )

        self.patient_id = patient_id
        self.disease = disease

    def display_patient(self):

        self.display_person()

        print("Patient ID:", self.patient_id)
        print("Disease:", self.disease)


class Doctor(Person):

    def __init__(self,
                 name,
                 age,
                 gender,
                 doctor_id,
                 specialization):

        Person.__init__(
            self,
            name,
            age,
            gender
        )

        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_doctor(self):

        self.display_person()

        print("Doctor ID:", self.doctor_id)
        print("Specialization:", self.specialization)


class Nurse(Person):

    def __init__(self,
                 name,
                 age,
                 gender,
                 nurse_id,
                 ward):

        Person.__init__(
            self,
            name,
            age,
            gender
        )

        self.nurse_id = nurse_id
        self.ward = ward

    def display_nurse(self):

        self.display_person()

        print("Nurse ID:", self.nurse_id)
        print("Ward:", self.ward)


# Objects

patient1 = Patient(
    "John",
    25,
    "Male",
    "P001",
    "Malaria"
)

doctor1 = Doctor(
    "Sarah",
    40,
    "Female",
    "D001",
    "Cardiology"
)

nurse1 = Nurse(
    "Peter",
    30,
    "Male",
    "N001",
    "Ward A"
)

print("\nPATIENT DETAILS")
patient1.display_patient()

print("\nDOCTOR DETAILS")
doctor1.display_doctor()

print("\nNURSE DETAILS")
nurse1.display_nurse()