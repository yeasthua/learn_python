stu_grades = {
    "Peter": 88,
    "Owen": 93,
    "Juneau": 98,
    }

total = 0
highest_grade = 0
top_student = ""

for name, grade in stu_grades.items():
    print(name, grade)

    total += grade

    if grade > highest_grade:
        highest_grade = grade
        top_student = name

average = total / len(stu_grades)

print("Average grade:", average)
print("Top Student:", top_student, "\n", "Highest grade:", highest_grade)

