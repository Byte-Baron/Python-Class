students = {}

for i in range(1, 4):
    class_name = input("Enter class name: ")
    print("\n")

    # Loop to get information for each student in the class
    for j in range(1, 6):
        student_name = input(f"Enter name of student {j} in {class_name} class: ")
        math = float(input(f"Enter math grade of {student_name} student: "))
        chemistry = float(input(f"Enter chemistry grade of {student_name} student: "))
        physics = float(input(f"Enter physics grade of {student_name} student: "))
        avrg = (math + chemistry + physics) / 3
        print()
        # Store student information in the dictionary
        students[student_name] = {
            "class": class_name,
            "math": math,
            "chemistry": chemistry,
            "physics": physics,
            "avrg": avrg
        }

print("\n")

# Print student information
print("-----------------------------------------------------------------------------------------------")
print("                                   Students Informations                                       ")
print("-----------------------------------------------------------------------------------------------")

for student, info in students.items():
    print(f"                                    Class: {info['class']}")
    print(f"                                    Name: {student}")
    print(f"                                    Math Grade: {info['math']}")
    print(f"                                    Chemistry Grade: {info['chemistry']}")
    print(f"                                    Physics Grade: {info['physics']}")
    print(f"                                    Average Grade: {info['avrg']}")
    print("\n")

print("-----------------------------------------------------------------------------------------------")
