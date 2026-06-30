import csv
import json
import os
import logging

# file names for storing data
CSV_FILE = "students.csv"
JSON_FILE = "students.json"
LOG_FILE = "student_system.log"


# custom exceptions for this program
class StudentNotFoundError(Exception):
    def __init__(self, reg_no):
        self.reg_no = reg_no
        super().__init__(f"No student found with registration number '{reg_no}'.")


class DuplicateStudentError(Exception):
    def __init__(self, reg_no):
        self.reg_no = reg_no
        super().__init__(f"Student '{reg_no}' already exists in the system.")


# set up logging to write actions into a log file
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def initialize_files():
    # create the csv and json files if they dont exist yet
    try:
        if not os.path.exists(CSV_FILE):

            with open(CSV_FILE, "w", newline="") as file:

                writer = csv.writer(file)
                writer.writerow(["Registration Number", "Name", "Age"])

        if not os.path.exists(JSON_FILE):

            with open(JSON_FILE, "w") as file:
                json.dump({}, file, indent=4)

    except (IOError, OSError) as error:
        logging.error(f"Could not create data files: {error}")
        print("Something went wrong setting up the files.")

    finally:
        logging.info("Checked data files.")


def read_csv_students():
    # read all students from the csv file
    students = []

    try:

        with open(CSV_FILE, "r", newline="") as file:

            reader = csv.reader(file)
            next(reader)  # skip the header row

            for row in reader:
                if len(row) >= 3:
                    students.append(row)

    except FileNotFoundError:
        logging.error(f"Could not find {CSV_FILE}")
        raise

    except (IOError, OSError, csv.Error) as error:
        logging.error(f"Problem reading csv file: {error}")
        raise

    return students


def read_json_details():
    # load the extra student details from json
    try:

        with open(JSON_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        logging.error(f"Could not find {JSON_FILE}")
        return {}

    except json.JSONDecodeError as error:
        logging.error(f"Json file is corrupted: {error}")
        print("The student details file seems corrupted.")
        return {}

    except (IOError, OSError) as error:
        logging.error(f"Problem reading json file: {error}")
        return {}


def save_json_details(details):
    # write updated details back to the json file
    try:

        with open(JSON_FILE, "w") as file:
            json.dump(details, file, indent=4)

    except (IOError, OSError) as error:
        logging.error(f"Could not save json file: {error}")
        print("Failed to save student details.")
        raise


def student_exists(reg_no):
    # check if a registration number is already in the csv
    students = read_csv_students()

    for row in students:
        if row[0] == reg_no:
            return True

    return False


def validate_age(age_input):
    # make sure age is a proper number
    try:

        age = int(age_input)

        if age <= 0 or age > 120:
            print("Please enter a valid age (1 to 120).")
            return None

        return str(age)

    except ValueError:
        print("Age must be a number.")
        return None


def show_student(reg_no, name, age, details):
    # print one student record
    print(f"Registration Number: {reg_no}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {details.get('address', 'N/A')}")
    print(f"Contact: {details.get('contact', 'N/A')}")
    print(f"Program: {details.get('program', 'N/A')}")


def display_menu():

    print("\n")
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def add_student():

    print("\n========== ADD NEW STUDENT ==========\n")

    reg_no = input("Enter Registration Number: ").strip()

    if reg_no == "":
        print("Registration number cannot be empty.")
        return

    name = input("Enter Student Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    age_input = input("Enter Age: ").strip()

    if age_input == "":
        print("Age cannot be empty.")
        return

    age = validate_age(age_input)

    if age is None:
        return

    address = input("Enter Address: ").strip()
    contact = input("Enter Contact Number: ").strip()
    program = input("Enter Program: ").strip()

    try:

        if student_exists(reg_no):
            raise DuplicateStudentError(reg_no)

        # save basic info to csv
        with open(CSV_FILE, "a", newline="") as file:

            writer = csv.writer(file)
            writer.writerow([reg_no, name, age])

        # save extra info to json
        students = read_json_details()

        students[reg_no] = {
            "address": address,
            "contact": contact,
            "program": program
        }

        save_json_details(students)

        logging.info(f"Added student: {reg_no}")
        print("\nStudent added successfully.")

    except DuplicateStudentError as error:

        print(f"\n{error}")
        logging.warning(f"Tried to add duplicate: {reg_no}")

    except (IOError, OSError, csv.Error) as error:

        print("\nCould not save the student record.")
        logging.error(f"Add failed for {reg_no}: {error}")

    finally:
        logging.info(f"Finished add operation for {reg_no}")


def view_students():

    print("\n========== ALL STUDENTS ==========\n")

    try:

        students = read_csv_students()

        if len(students) == 0:
            print("No students in the system yet.")
            return

        extra = read_json_details()

        for row in students:

            reg_no = row[0]
            name = row[1]
            age = row[2]
            details = extra.get(reg_no, {})

            show_student(reg_no, name, age, details)
            print("-" * 40)

        logging.info("Viewed all students")

    except FileNotFoundError:

        print("No data file found. Add a student first.")
        logging.error("View failed - csv missing")

    except (IOError, OSError) as error:

        print("Could not read student records.")
        logging.error(f"View failed: {error}")

    finally:
        logging.info("Finished view operation")


def search_student():

    print("\n========== SEARCH STUDENT ==========\n")

    reg_no = input("Enter Registration Number: ").strip()

    if reg_no == "":
        print("Registration number cannot be empty.")
        return

    try:

        students = read_csv_students()
        found = False
        name = ""
        age = ""

        for row in students:

            if row[0] == reg_no:
                found = True
                name = row[1]
                age = row[2]
                break

        if not found:
            raise StudentNotFoundError(reg_no)

        extra = read_json_details()
        details = extra.get(reg_no, {})

        print("\nStudent found:")
        show_student(reg_no, name, age, details)

        logging.info(f"Searched for {reg_no}")

    except StudentNotFoundError as error:

        print(f"\n{error}")
        logging.warning(f"Search failed - {reg_no} not found")

    except FileNotFoundError:

        print("No data file found.")
        logging.error("Search failed - csv missing")

    except (IOError, OSError) as error:

        print("Could not search records.")
        logging.error(f"Search failed: {error}")

    finally:
        logging.info(f"Finished search for {reg_no}")


def update_student():

    print("\n========== UPDATE STUDENT ==========\n")

    reg_no = input("Enter Registration Number to update: ").strip()

    if reg_no == "":
        print("Registration number cannot be empty.")
        return

    try:

        students = read_csv_students()
        found = False
        current_name = ""
        current_age = ""

        for row in students:

            if row[0] == reg_no:
                found = True
                current_name = row[1]
                current_age = row[2]

        if not found:
            raise StudentNotFoundError(reg_no)

        extra = read_json_details()
        current_details = extra.get(reg_no, {})

        print(f"\nUpdating {reg_no}")
        print("Press Enter to keep the current value.\n")

        new_name = input(f"Name [{current_name}]: ").strip()
        new_age = input(f"Age [{current_age}]: ").strip()
        new_address = input(f"Address [{current_details.get('address', '')}]: ").strip()
        new_contact = input(f"Contact [{current_details.get('contact', '')}]: ").strip()
        new_program = input(f"Program [{current_details.get('program', '')}]: ").strip()

        if new_name != "":
            current_name = new_name

        if new_age != "":

            checked_age = validate_age(new_age)

            if checked_age is None:
                return

            current_age = checked_age

        if new_address != "":
            current_details["address"] = new_address

        if new_contact != "":
            current_details["contact"] = new_contact

        if new_program != "":
            current_details["program"] = new_program

        # rewrite csv with updated info
        with open(CSV_FILE, "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(["Registration Number", "Name", "Age"])

            for row in students:

                if row[0] == reg_no:
                    writer.writerow([reg_no, current_name, current_age])
                else:
                    writer.writerow(row)

        extra[reg_no] = current_details
        save_json_details(extra)

        logging.info(f"Updated student: {reg_no}")
        print("\nStudent updated successfully.")

    except StudentNotFoundError as error:

        print(f"\n{error}")
        logging.warning(f"Update failed - {reg_no} not found")

    except (IOError, OSError, csv.Error) as error:

        print("Could not update the record.")
        logging.error(f"Update failed for {reg_no}: {error}")

    finally:
        logging.info(f"Finished update for {reg_no}")


def delete_student():

    print("\n========== DELETE STUDENT ==========\n")

    reg_no = input("Enter Registration Number to delete: ").strip()

    if reg_no == "":
        print("Registration number cannot be empty.")
        return

    try:

        students = read_csv_students()
        found = False
        remaining = []

        for row in students:

            if row[0] == reg_no:
                found = True
            else:
                remaining.append(row)

        if not found:
            raise StudentNotFoundError(reg_no)

        confirm = input(f"\nDelete {reg_no}? Type yes to confirm: ").strip().lower()

        if confirm != "yes":
            print("\nDelete cancelled.")
            logging.info(f"User cancelled delete for {reg_no}")
            return

        # remove from csv
        with open(CSV_FILE, "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(["Registration Number", "Name", "Age"])
            writer.writerows(remaining)

        # remove from json
        extra = read_json_details()

        if reg_no in extra:
            del extra[reg_no]

        save_json_details(extra)

        logging.info(f"Deleted student: {reg_no}")
        print("\nStudent deleted.")

    except StudentNotFoundError as error:

        print(f"\n{error}")
        logging.warning(f"Delete failed - {reg_no} not found")

    except (IOError, OSError, csv.Error) as error:

        print("Could not delete the record.")
        logging.error(f"Delete failed for {reg_no}: {error}")

    finally:
        logging.info(f"Finished delete for {reg_no}")


def main():

    initialize_files()
    logging.info("Program started")

    while True:

        try:

            display_menu()
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                update_student()

            elif choice == "5":
                delete_student()

            elif choice == "6":

                print("\nThank you for using the system.")
                logging.info("Program closed")
                break

            else:

                print("\nInvalid choice. Pick a number from 1 to 6.")
                logging.warning(f"Bad menu choice: {choice}")

        except KeyboardInterrupt:

            print("\n\nExiting...")
            logging.warning("User pressed Ctrl+C")
            break

        except Exception as error:

            print("\nSomething went wrong. Try again.")
            logging.error(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
