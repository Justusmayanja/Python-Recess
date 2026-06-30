class User:

    def __init__(self, first_name, last_name, age, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.email = email

    def describe_user(self):
        print("\nUser Information")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Country:", self.country)
        print("Email:", self.email)

    def greet_user(self):
        print("Welcome,", self.first_name + "!")


user1 = User("John", "Peter", 21, "Uganda", "john@gmail.com")
user2 = User("Sarah", "Namusoke", 23, "Kenya", "sarah@gmail.com")
user3 = User("David", "Okello", 25, "Tanzania", "david@gmail.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()