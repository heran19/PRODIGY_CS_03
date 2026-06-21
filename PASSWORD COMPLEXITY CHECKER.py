import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    strength_levels = {
        0: "Very Weak", 1: "Very Weak", 2: "Weak",
        3: "Moderate", 4: "Strong", 5: "Very Strong"
    }

    return strength_levels[score], feedback

password = input("Enter a password to check: ")
strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if feedback:
    print("Suggestions:")
    for f in feedback:
        print(f"- {f}")
else:
    print("Great password!")
