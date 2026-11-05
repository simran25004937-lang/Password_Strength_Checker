from password_pkg import check_length, character_score, strength_result

print("======================================")
print("       PASSWORD STRENGTH CHECKER")
print("======================================")

password = input("Enter a sample password: ")

try:
    length = check_length(password)
    score = character_score(password)
    result = strength_result(password)

    print("\n--------- PASSWORD REPORT ---------")
    print("Password Length:", len(password))
    print("Length Valid:", "Yes" if length else "No")
    print("Character Variety Score:", score, "/ 4")
    print("Password Strength:", result)

except (ValueError, TypeError) as error:
    print("Error:", error)

print("======================================")