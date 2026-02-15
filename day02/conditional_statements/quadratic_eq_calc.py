#A simple quadratic equation calculator
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Quadratic formula (-b ± sqrt(b²-4ac))/(2a)
root1 = float((-b + sqrt(pow(b,2) - 4 *a *c)) / (2 * a))
root2 = float((-b - sqrt(pow(b,2) - 4 *a *c)) / (2 * a))

print("The roots are", root1, " and", root2)
