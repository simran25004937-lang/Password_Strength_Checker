
# Password Strength Checker

# Function 1: Check password length
def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False


# Function 2: Calculate character variety score
def character_score(password):
    score = 0

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    return score


# Function 3: Check password strength
def strength_result(password):
    if not password:
        return "Password cannot be empty"

    length = check_length(password)
    score = character_score(password)

    if length and score == 4:
        return "Strong Password"

    elif length and score >= 2:
        return "Medium Password"

    else:
        return "Weak Password"