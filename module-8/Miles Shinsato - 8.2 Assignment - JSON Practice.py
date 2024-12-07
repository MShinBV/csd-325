# Miles Shinsato 12/06/2024 CSD-325 A339 Module 8.2 Assignment - JSON Practice

# Import JSON prompt
import json

# Defining file_path as 'student.json'
file_path = 'student.json'

# Load JSON file as a python list
with open('student.json') as f:
    ClassList = json.load(f)

# Defining print_student_list function
def print_student_list():
    index = 0
    for i in ClassList:
        student = ClassList[index]
        # Formating for how student information should be displayed
        print(f'{student["L_Name"]}, {student["F_Name"]}: ID= {student["Student_ID"]}, Email = {student["Email"]}')
        index += 1


# Defining add_miles function
def add_miles():

    # Creating placeholder for Miles information
    # Adding values for each part of the students table for Miles
    new_student = {
        'F_Name': 'Miles',
        'L_Name': 'Shinsato',
        'Student_ID': '2045',
        'Email': 'Miles@email.com'
    }

    # Appending new_student to end of Class list
    ClassList.append(new_student)

# Defining update_student_file function to add to students list
def update_student_list ():

    # Opens student.json file to write 'w' mode to overwrite the file with changes
    with open(file_path, "w") as file:

        # Writes back to student.json file with indent=4 formats with 4 spaces
        json.dump(ClassList, file, indent=4)

    # Print message to show that student.json was updated
    print('\nstudent.json has been updated.\n')

# Start of Main loop
def main():

    # Print message to show original student list
    print('\n---This is the original student list---')
    print('Original Student List:')

    # Prompt to print_student_list function
    print_student_list()

    # Prompt to run add_miles
    add_miles()

    # Function to print Updated Student List
    print('\n---This is an updated student list---')
    print('Updated student list:')

    # Prompt to print_student_list after add_miles is run
    print_student_list()

    # Prompt to run update_student_list
    update_student_list()


if __name__ == '__main__':
    main()