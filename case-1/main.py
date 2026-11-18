# Project 01: Progressive Electricity Billing
# Concepts used: input/output, variables, type conversion,
# arithmetic operators, relational operators, and if-elif-else.

print("PROGRESSIVE ELECTRICITY BILLING")
print("--------------------------------")

units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid input: units cannot be negative.")
else:
    energy_charge = 0.0

    # Calculate the charge using progressive consumption slabs.
    if units <= 100:
        energy_charge = units * 1.50
    else:
        energy_charge = 100 * 1.50

        if units <= 200:
            energy_charge = energy_charge + (units - 100) * 2.50
        else:
            energy_charge = energy_charge + 100 * 2.50

            if units <= 400:
                energy_charge = energy_charge + (units - 200) * 4.00
            else:
                energy_charge = energy_charge + 200 * 4.00
                energy_charge = energy_charge + (units - 400) * 6.00

    fixed_charge = 50.00
    surcharge = 0.0
    rebate = 0.0

    if energy_charge > 1000:
        surcharge = energy_charge * 0.05
    elif units <= 100:
        rebate = energy_charge * 0.02

    final_bill = energy_charge + fixed_charge + surcharge - rebate

    print("\n----------- BILL SUMMARY -----------")
    print("Units consumed       :", units)
    print("Energy charge        : Rs.", round(energy_charge, 2))
    print("Fixed charge         : Rs.", round(fixed_charge, 2))
    print("Surcharge             : Rs.", round(surcharge, 2))
    print("Rebate                : Rs.", round(rebate, 2))
    print("------------------------------------")
    print("Final bill amount     : Rs.", round(final_bill, 2))
    print("------------------------------------")
