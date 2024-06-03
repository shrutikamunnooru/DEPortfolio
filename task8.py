'''
Write a Python program to manage student records. Each student has a name, age, and a list of grades. 
implement functions to add a new student, remove a student, update student grades, and calculate the average grade 
for a student.
'''

def add_student(students, name, age):
    students.append([name, age, []])
    print(f"Student {name} added successfully.")

def remove_student(students, name):
    for student in students:
        if student[0] == name:
            students.remove(student)
            print(f"Student {name} removed successfully.")
            return
    print(f"Student {name} not found.")

def update_grades(students, name, grades):
    for student in students:
        if student[0] == name:
            student[2] = grades
            print(f"Grades updated for student {name}.")
            return
    print(f"Student {name} not found.")

def calculate_average(students, name):
    for student in students:
        if student[0] == name:
            if student[2]:
                avg = sum(student[2]) / len(student[2])
                print(f"Average grade for student {name} is {avg:.2f}.")
                return avg
            else:
                print(f"No grades available for student {name}.")
                return None
    print(f"Student {name} not found.")


if __name__ == "__main__":
    students = []

    # Adding students
    add_student(students, "Rina", 20)
    add_student(students, "Mina", 21)
    add_student(students, "Tina", 21)

    # Removing a student
    remove_student(students, "Rina")

    # Updating grades
    update_grades(students, "Mina", [89, 79, 90])
    update_grades(students, "Tina", [70, 80, 85])

    # Calculating average grades
    calculate_average(students, "Mina")
    calculate_average(students, "Tina")

   

