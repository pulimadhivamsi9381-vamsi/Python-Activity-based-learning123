# Project 06: Password Policy Validation Engine
password = input("Enter a password to check: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    else:
        has_special = True

length_ok = len(password) >= 8

print("\nPASSWORD POLICY CHECK")
print("At least 8 characters :", length_ok)
print("Contains uppercase    :", has_upper)
print("Contains lowercase    :", has_lower)
print("Contains a digit      :", has_digit)
print("Contains special char :", has_special)

if length_ok and has_upper and has_lower and has_digit and has_special:
    print("Result: VALID PASSWORD")
else:
    print("Result: INVALID PASSWORD")
