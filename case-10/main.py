# Project 10: Food Waste Monitoring System
total_prepared = 0.0
total_wasted = 0.0
valid = True

print("FOOD WASTE MONITORING - 3 DAYS")
for day in range(1, 4):
    prepared = float(input("Day " + str(day) + " - food prepared (kg): "))
    wasted = float(input("Day " + str(day) + " - food wasted (kg): "))

    if prepared <= 0 or wasted < 0 or wasted > prepared:
        valid = False
    else:
        total_prepared = total_prepared + prepared
        total_wasted = total_wasted + wasted

if not valid:
    print("Invalid input: prepared quantity must be positive and waste must be between zero and prepared quantity.")
else:
    waste_percentage = total_wasted / total_prepared * 100

    if waste_percentage < 5:
        category = "LOW"
    elif waste_percentage <= 10:
        category = "MODERATE"
    else:
        category = "HIGH"

    print("\nFOOD WASTE REPORT")
    print("Total food prepared:", round(total_prepared, 2), "kg")
    print("Total food wasted  :", round(total_wasted, 2), "kg")
    print("Waste percentage   :", round(waste_percentage, 2), "%")
    print("Waste level        :", category)
