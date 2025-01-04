students = int(input("Input number of students"))

grade_sum = 0
all_grades =[]
student_num = 1
for student in range(students):
    grade = int(input(f"Enter grades on 00-100 scale for student #{student_num}"))
    all_grades.append(grade)
    student_num += 1

average = sum(all_grades)/len(all_grades)

print("Average:", average)
print("Min:", min(all_grades))
print("Max:", max(all_grades))
print("All grades:", all_grades)
