# Topic 3: Functions

def calculate_average(marks_list):
    """Takes a list of marks and returns the average."""
    return sum(marks_list) / len(marks_list)


def get_grade(average):
    """Takes an average and returns a grade string."""
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"


def greet_student(name, grade):
    """Prints a personalized greeting with the grade."""
    print(f"Hello {name}, your grade is {grade}. Well done!")



name = input("Enter your name: ")
marks = [85, 90, 78]  

avg = calculate_average(marks)
grade = get_grade(avg)

print(f"\nAverage: {avg:.2f}")
greet_student(name, grade)