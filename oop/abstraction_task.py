from abc import ABC, abstractmethod     # Imports abstract base class to create "blueprint" for other subclasses

# global variables
name = input("Enter your name: ")
sub1 = int(input("Enter your grade (sub 1): "))
sub2 = int(input("Enter your grade (sub 2): "))
sub3 = int(input("Enter your grade (sub 3): "))

# Base class (blueprint)
class Student(ABC):
    def __init__(self, name, sub1, sub2, sub3):     # Initialize attributes when object is created
        self.name = name
        self.score = [sub1, sub2, sub3]
        
    @abstractmethod     # Forces subclasses to implement the method
    def compute_average(self):
        pass       # Allows subclasses to provide its own specific implementation of the method
        
    @abstractmethod
    def get_status(self):
        pass

# Subclass inherits from (Student)
class Person(Student):

    def compute_average(self):
        return sum(self.score) // len(self.score)   # Specific implementation of the method


    def get_status(self):
        avg = self.compute_average()

        if avg < 75:
            return "Failed"
        else:
            return "Passed"

# Declaring an object
person = Person(name, sub1, sub2, sub3)

# Display information
print("\n")
print("Your Information")
print(f"Name: {person.name}")
print(f"Average: {person.compute_average()}")
print(f"Status: {person.get_status()}")