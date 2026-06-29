def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

name = input("Enter student name: ")
marks = float(input("Enter marks (out of 100): "))

grade = calculate_grade(marks)
print(f"\nStudent: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
