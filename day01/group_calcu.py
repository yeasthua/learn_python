# Group calculator (If the division is not even, one of the groups may have fewer members than specified.)
course_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

#Adding (group_size - 1) ensures that any leftover students
# creates an extra group instead of being discarded.
number_of_groups = (course_students + group_size - 1) // group_size

print(f"Number of groups formed: {number_of_groups}")