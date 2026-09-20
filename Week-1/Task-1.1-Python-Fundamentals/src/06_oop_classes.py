# Topic 6: Object-Oriented Programming (OOP) - Classes

class Student:
    """Represents a single student with a name and a list of marks."""

    def __init__(self, name, marks):
        # __init__ runs automatically when a new Student is created
        self.name = name
        self.marks = marks

    def get_average(self):
        """Returns the average of this student's marks."""
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        """Returns a grade based on the average."""
        avg = self.get_average()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        else:
            return "C"

    def display(self):
        """Prints a summary of this student."""
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Grade: {self.get_grade()}\n")


# --- Using the class ---
student1 = Student("Rakshitha", [85, 90, 78])
student2 = Student("Amit", [60, 55, 70])

student1.display()
student2.display()

# Why a class makes sense here:
# Each student "object" bundles together its own data (name, marks)
# AND its own behavior (get_average, get_grade) in one place,
# instead of managing separate lists/dictionaries and loose functions.