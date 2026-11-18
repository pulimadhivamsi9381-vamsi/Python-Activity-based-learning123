# Project 02: Examination Result and Grace-Mark Validation
print("EXAMINATION RESULT")
marks = []
for subject in range(1, 6):
    mark = float(input("Enter marks for subject " + str(subject) + " (0-100): "))
    marks.append(mark)

valid = True
for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if not valid:
    print("Invalid input: marks must be between 0 and 100.")
else:
    adjusted = marks.copy()
    failed_count = 0
    failed_index = -1

    for index in range(5):
        if adjusted[index] < 35:
            failed_count = failed_count + 1
            failed_index = index

    grace = 0
    if failed_count == 1 and adjusted[failed_index] >= 30:
        grace = 35 - adjusted[failed_index]
        adjusted[failed_index] = 35

    total = 0
    passed = True
    for mark in adjusted:
        total = total + mark
        if mark < 35:
            passed = False

    percentage = total / 5
    print("\nOriginal marks:", marks)
    print("Adjusted marks:", adjusted)
    print("Grace marks awarded:", grace)
    print("Total:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")
