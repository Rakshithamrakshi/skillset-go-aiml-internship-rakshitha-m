# Topic 2: Conditions and Loops - Grade Calculator

num_subjects = int(input("How many subjects? "))
total = 0

for i in range(num_subjects):
    marks = float(input(f"Enter marks for subject {i+1} (out of 100): "))
    total += marks

average = total / num_subjects

print(f"\nTotal Marks: {total}")
print(f"Average: {average:.2f}")

# Grading logic using if/elif/else
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade: {grade}")

# while loop example - countdown
print("\nCountdown:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Done!")