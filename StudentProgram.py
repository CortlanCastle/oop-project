import StudentClass as sc

def main():
    student_id = input('Enter student ID: ')
    name = input('Enter student name: ')
    dob = input('Enter date of birth (MM/DD/YYYY): ')
    classification = input('Enter student classification (Freshman, Sophmore, Junior, Senior): ')

    student = sc.Student(student_id, name, dob, classification)

    print('Student ID:', student.get_student_id())
    print('Student Name:', student.get_name())
    print('Date of Birth:', student.get_dob())
    print('Classification:', student.get_classification())
    print('Student Age:', student.calculate_age())
    print('Registration Dates:', student.determine_registration_date())

main()