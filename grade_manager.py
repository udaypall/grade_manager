# Student Grade Calculator


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "E"


def get_marks():
    while True:
        try:
            marks = float(input("Enter total marks (0-100): "))

            if marks < 0:
                print("Marks cannot be negative.")

            if marks > 100:
                print("Marks cannot be greater than 100.")

            return marks

        except ValueError as e:
            print("Invalid input:", e)

        finally:
            print("Marks validation completed.")


# Get number of students
while True:
    try:
        no_of_students = int(input("Enter number of students: "))

        if no_of_students <= 0:
            print("Number of students must be greater than 0.")

        break

    except ValueError as e:
        print("Invalid input:", e)

    finally:
        print("Student count validation completed.")


# Store student details
students = []

for i in range(no_of_students):

    print(f"\nEnter details for Student {i + 1}")

    name = input("Enter student name: ")

    marks = get_marks()

    grade = calculate_grade(marks)

    student = {
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)


# Display student results

print(f"{'Name':<20}{'Marks':<12}{'Grade':<10}")


for student in students:
    print(
        f"{student['name']:<20}"
        f"{student['marks']:<12.2f}"
        f"{student['grade']:<10}"
    )




total_marks = sum(student["marks"] for student in students)
average_marks = total_marks / len(students)

highest_mark = max(student["marks"] for student in students)
lowest_mark = min(student["marks"] for student in students)


print(f"Average Marks: {average_marks:.2f}", f"  Highest Mark: {highest_mark:.2f}", f"   Lowest Mark: {lowest_mark:.2f}")

