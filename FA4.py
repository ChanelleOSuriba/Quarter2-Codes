class_total = 0
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))
for student in range(1, num_students + 1):
    print(f"Student {student}")
    total = 0

    for subject in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        total += score

    average = total / num_subjects
    print(f"Average for Student {student} = {average}")

    class_total += average

class_average = class_total / num_students
print(f"Class Average = {class_average}")
