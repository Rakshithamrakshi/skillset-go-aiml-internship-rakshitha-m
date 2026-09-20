# Topic 1: Variables and Data Types

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
is_student = True

print("\n--- Your Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "cm")
print("Is student:", is_student)

print("\nData types used:")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))