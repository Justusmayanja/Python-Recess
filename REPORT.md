Student Record Management System  Report

Name: Mayanja Justus 24/U/06735/PS
Course: Software Engineering
Date: June 29, 2026


Program Design

For this assignment I built a simple menu-driven program in Python that helps manage student records from the command line. When you run it, you get six options: add a student, view all students, search by registration number, update details, delete a record, or exit.

I decided to store the data in two separate files. The main student info goes into students.csv — that file holds the registration number, name, and age. I used CSV because it is straightforward and you can even open it in Excel if you want to check the data quickly.

The extra details like address, phone number, and program go into students.json. Each student is stored under their registration number as the key. I kept these separate so the CSV stays clean and small, while the JSON can hold the other fields without making the spreadsheet messy.

Every time someone uses the system, actions get written to student_system.log. If something goes wrong later, you can open that file and see what happened.

When the program starts, it runs initialize_files() first to make sure both data files exist. After that, main() keeps showing the menu in a loop until the user picks option 6 to exit.


Key Functions

The program is split into a few helper functions and the main menu actions.

initialize_files() creates students.csv and students.json if they are not already there. read_csv_students() opens the CSV and returns all the student rows. read_json_details() loads the JSON file and gives back the extra details. save_json_details() writes changes back to the JSON file.

student_exists() checks whether a registration number is already taken before adding someone new. validate_age() makes sure the age entered is actually a number and within a reasonable range. display_student_record() just prints out one student's full details in a readable way.

For the actual menu options, add_student() takes input from the user and saves the record to both files. view_students() reads everything and displays all students one by one. search_student() looks up a single student by registration number. update_student() lets you change details — if you press Enter on a field, it keeps the old value. delete_student() removes a student, but only after you type yes to confirm.

I put the file reading and writing into helper functions so I did not have to repeat the same open-and-read code in every menu option.


Exception Handling

The assignment required try, except, finally, and a custom exception, so I used those throughout the program.

I created two custom exceptions. StudentNotFoundError is raised when you try to search, update, or delete a student who does not exist. DuplicateStudentError is raised when you try to add a student whose registration number is already in the system.

For built-in errors, the program catches FileNotFoundError if a data file is missing, IOError and OSError when reading or writing fails, json.JSONDecodeError if the JSON file gets corrupted, csv.Error if the CSV cannot be read properly, and ValueError when someone enters text instead of a number for age. There is also a handler for KeyboardInterrupt so the program exits cleanly if the user presses Ctrl+C.

Most of the menu functions use a finally block to log that the operation finished, whether it worked or not. That way the log file always shows when something was attempted.

Before touching any files, the program checks basic input — empty registration numbers and names are rejected, age has to be a real number between 1 and 120, and delete asks for confirmation so you do not remove someone by accident.


Logging

I set up logging at the start of the program using Python's logging module. Everything goes into student_system.log with a timestamp and a message.

Normal actions like adding, updating, deleting, or searching a student are logged as INFO. Things like a duplicate registration number, a student not found, or a wrong menu choice go in as WARNING. Actual problems — file errors, bad JSON, unexpected crashes — are logged as ERROR.

This made testing easier because I could run a few options and then check the log to confirm everything was recorded correctly.


Testing

I tested the program using the four sample students already in students.csv and students.json.

First I chose option 2 to view all students. All four records showed up with both the CSV fields and the JSON details like address and program. That worked as expected.

For search, I entered REG002 and the program found Jane Smith with all her details. I also tried REG999, which is not in the system, and got the not found message. Both cases behaved correctly.

When adding a student, I tried REG001 again and the program stopped me with the duplicate error. Then I added a new student with REG005 and checked both files — the record appeared in CSV and JSON.

For update, I changed the name for REG003 and confirmed the change was saved in both files. I also tried entering "abc" as an age when adding a student and the program rejected it with a validation message.

For delete, I removed REG005 after typing yes, and it was gone from both files. When I typed no on another delete attempt, the record stayed and the program just said delete cancelled.

I entered 9 at the menu once to test invalid input, and the program told me to pick a number from 1 to 6. Finally I chose option 6 to exit and the log showed "Program Closed."

Everything I tested passed. The entries in student_system.log matched what I did during the test run.


Conclusion

Overall the system does what the assignment asked for. It stores records in CSV and JSON, supports all the CRUD operations through a menu, handles errors with try/except/finally and custom exceptions, logs user actions and errors, and validates input before saving data. Splitting basic info and extra details across two files kept the design simple while still storing everything the program needs.
