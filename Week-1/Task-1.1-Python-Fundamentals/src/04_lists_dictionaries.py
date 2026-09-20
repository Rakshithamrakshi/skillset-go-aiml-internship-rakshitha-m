# Topic 4: Lists and Dictionaries - Student Records

# A list of dictionaries - each dictionary is one student's record
students = [
    {"name": "Amit", "marks": [85, 90, 78]},
    {"name": "Priya", "marks": [92, 88, 95]},
    {"name": "Rakshitha", "marks": [70, 65, 80]},
]

print("--- Student Records ---\n")

for student in students:
    name = student["name"]
    marks = student["marks"]
    average = sum(marks) / len(marks)
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}\n")

# Find the topper (student with highest average)
topper = None
highest_avg = 0

for student in students:
    avg = sum(student["marks"]) / len(student["marks"])
    if avg > highest_avg:
        highest_avg = avg
        topper = student["name"]

print(f"Topper: {topper} with average {highest_avg:.2f}")

# Adding a new student to the list
new_student = {"name": "Karan", "marks": [60, 55, 70]}
students.append(new_student)
print(f"\nTotal students after adding one: {len(students)}")