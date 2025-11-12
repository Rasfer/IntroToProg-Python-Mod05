# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   REidswick, 11/11/2025, modified script 
# ------------------------------------------------------------------------------------------ #

# Import libraries
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  = '' # Hold the choice made by the user.

try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script.")
    print("Techincal error message:")
    print(e, e.__doc__, type(e), sep='\n')
    file = open(FILE_NAME, 'w') # Creates the file if it didn't exists
    file.write(json.dumps(students, indent=4)) # Creates the format for a list in the json file
    file.close()
except Exception as e:
    print("There was a non specific error")
    print("Techincal error message:")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Input dat
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must be a letter")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must be a letter")

            course_name = input("Enter course name: ")
            # Creates the dictionary and loads it into the list
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f'You have registered {student_data["FirstName"]} {student_data["LastName"]} for '
                  f'{student_data["CourseName"]}.')

        # Exceptions
        except ValueError as e:
            print(e)
            print("-- Technical error message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error")
            print("Technical error message:")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}.')
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file, indent=4)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical error message --")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non specific error")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
        print("Data Saved!")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
