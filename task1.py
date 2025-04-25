# dictionary of names and marks
student_report = {'Alice' : 85, 'Bob' : 75, 'Cadel' : 90, 'Daisy' : 97, 'Ethan' : 68}

input_name = input("Enter the student's name: ")
if input_name.capitalize() in student_report:
    print("{}'s marks: {}".format(input_name.capitalize(), student_report[input_name.capitalize()]))

else:
    print('Student not found.')