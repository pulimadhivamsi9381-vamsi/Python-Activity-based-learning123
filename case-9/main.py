# Project 09: Student Marks Matrix Analysis
marks = []
valid = True

print("Enter marks for 3 students in 3 subjects (0-100).")
for student in range(1, 4):
    row = []
    for subject in range(1, 4):
        mark = float(input("Student " + str(student) +
                           ", Subject " + str(subject) + ": "))
        if mark < 0 or mark > 100:
            valid = False
        row.append(mark)
    marks.append(row)

if not valid:
    print("Invalid input: every mark must be between 0 and 100.")
else:
    print("\nMARKS MATRIX")
    for row in marks:
        print(row)

    print("\nSTUDENT TOTALS AND AVERAGES")
    for index in range(3):
        total = 0
        for mark in marks[index]:
            total = total + mark
        average = total / 3
        print("Student", index + 1, "- Total:", total,
              "Average:", round(average, 2))

    print("\nHIGHEST MARK IN EACH SUBJECT")
    for subject_index in range(3):
        highest = marks[0][subject_index]
        for student_index in range(1, 3):
            if marks[student_index][subject_index] > highest:
                highest = marks[student_index][subject_index]
        print("Subject", subject_index + 1, ":", highest)
