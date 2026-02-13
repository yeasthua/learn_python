# Printing with F-Strings
name = "Yeasthua"
age = 18
skill1 = "python"
level1 = "beginner"
skill2 = "c++"
level2 = "beginner"
skill3 = "programming"
level3 = "noobie"
lower = 20000
upper = 50000

print(f"my name is {name}, I am {age} years old\n")

print(f"my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} pesos per month")


# Printing arithmetic operations using f-strings
x = 27
y = 15

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")