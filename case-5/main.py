# Project 05: Repeated Transaction Detection
accepted_references = []

print("REPEATED TRANSACTION DETECTION")
print("Enter 8 transaction reference numbers.")

for count in range(1, 9):
    reference = input("Reference " + str(count) + ": ")

    if reference in accepted_references:
        print("DUPLICATE: This reference was already entered.")
    else:
        accepted_references.append(reference)
        print("ACCEPTED: New transaction reference.")

print("\nUnique references:", accepted_references)
print("Number of unique transactions:", len(accepted_references))
