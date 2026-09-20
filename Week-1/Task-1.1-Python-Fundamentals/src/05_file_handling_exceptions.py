# Topic 5: File Handling and Exception Handling

# --- Part 1: Writing to a file ---
students = [
    {"name": "Amit", "marks": [85, 90, 78]},
    {"name": "Priya", "marks": [92, 88, 95]},
]

with open("students_data.txt", "w") as file:
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        file.write(f"{student['name']}: {avg:.2f}\n")

print("Data written to students_data.txt successfully.")

# --- Part 2: Reading from the file ---
print("\n--- Reading back the file ---")
with open("students_data.txt", "r") as file:
    contents = file.read()
    print(contents)

# --- Part 3: Handling a missing file (exception handling) ---
print("--- Testing a missing file ---")
try:
    with open("this_file_does_not_exist.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error handled: The file does not exist. Continuing safely.")

# --- Part 4: Handling invalid input (exception handling) ---
print("\n--- Testing invalid input ---")
try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Error handled: That wasn't a valid number.")