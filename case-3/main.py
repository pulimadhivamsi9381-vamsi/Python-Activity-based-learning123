# Project 03: Attendance Recovery Computation
print("ATTENDANCE RECOVERY")
conducted = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid class counts.")
else:
    percentage = attended / conducted * 100
    print("Current attendance:", round(percentage, 2), "%")

    if percentage >= 75:
        print("You have already reached the required attendance.")
        print("Additional classes required: 0")
    else:
        additional = 0
        while ((attended + additional) / (conducted + additional)) * 100 < 75:
            additional = additional + 1

        print("Required attendance: 75%")
        print("Additional consecutive classes to attend:", additional)
        print("Attendance after recovery:",
              round((attended + additional) / (conducted + additional) * 100, 2), "%")
