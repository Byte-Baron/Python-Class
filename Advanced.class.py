students = {}

for i in range(1, 4):
    class_name = input("Enter class name: ")
    print("\n")

    # Loop to get information for each student in the class
    for j in range(1, 6):
        student_name = input(f"Enter name of student {j} in {class_name} class: ")
        math_grade = float(input(f"Enter math grade of {student_name} student: "))
        chemistry_grade = float(input(f"Enter chemistry grade of {student_name} student: "))
        physics_grade = float(input(f"Enter physics grade of {student_name} student: "))

        # Calculate average grade
        average_grade = (math_grade + chemistry_grade + physics_grade) / 3

        # Store student information in the dictionary
        students[student_name] = {
            "class": class_name,
            "math_grade": math_grade,
            "chemistry_grade": chemistry_grade,
            "physics_grade": physics_grade,
            "average_grade": average_grade
        }

print("\n")

# Print student information
print("-----------------------------------------------------------------------------------------------")
print("                                   Students Informations                                       ")
print("-----------------------------------------------------------------------------------------------")

for student, info in students.items():
    print(f"                                    Class: {info['class']}")
    print(f"                                    Name: {student}")
    print(f"                                    Math Grade: {info['math_grade']}")
    print(f"                                    Chemistry Grade: {info['chemistry_grade']}")
    print(f"                                    Physics Grade: {info['physics_grade']}")
    print(f"                                    Average Grade: {info['average_grade']}")
    print("\n")

print("-----------------------------------------------------------------------------------------------")
