from abc import ABC, abstractmethod     # Imports abstract base class to create "blueprint" for subclasses

# Base class (blueprint)
class Employee(ABC):
    
    def __init__ (self, name):      # Initialize shared attribute for all employees
        self.name = name

    @abstractmethod                 # Forces subclasses to implement this method
    def compute_salary(self):
        pass

# Subclass 1 (Fixed salary)
class RegularEmployee (Employee):

    def __init__(self, name, salary):
        super().__init__(name)      # Calls parent's __init__ to set self.name
        self.salary = salary        # Unique attribute for regular employees

    def compute_salary(self):
        return self.salary          # Fixed salary, no calculations needed

# Subclass 2 (rate * hours)
class PartTimeEmployee (Employee):

    def __init__(self, name, rate, hours):
        super().__init__(name)      # Calls parent's __init__ to set self.name
        self.rate = rate            # Unique attributes for part-time employees
        self.hours = hours

    def compute_salary(self):
        return self.rate * self.hours   # Salary = rate per hour * hours worked

# User input    
name = input("Enter your name: ")
salary = int(input("Enter your monthly salary: "))
rate = int(input("Rate per hour: "))
hours = int(input("Hours worked: "))

# Creating objects for each employee type
regular = RegularEmployee(name, salary)
part_time = PartTimeEmployee(name, rate, hours)

# Display employee details
print("\n")
print("Employee Details:")
print(f"Name: {name}")
print(f"Regular salary: {regular.compute_salary()}")
print(f"Part-time salary: {part_time.compute_salary()}")