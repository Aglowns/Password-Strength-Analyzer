import re

def password_strength(password):
    # Initialize score
    score = 0

    # Check for length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Check for uppercase and lowercase characters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+=\-{}[\]:;"\'<>,.?/]', password):
        score += 1

    # Avoid common patterns (sequences of 3 or more)
    if re.search(r'(.)\1\1', password):  # detects three repeating characters
        score -= 1

    # Avoid dictionary words (basic)
    dictionary_words = ["password", "123456", "qwerty", "letmein", "welcome"]
    for word in dictionary_words:
        if word in password.lower():
            score -= 1

    # Provide feedback based on score
    if score <= 1:
        return "Weak password. Try to make it longer and include diverse characters."
    elif score == 2:
        return "Fair password. Could use more variety and length."
    elif score == 3:
        return "Good password. Adding more length and special characters could improve it."
    elif score >= 4:
        return "Strong password!"

# Test the analyzer
user_password = input("Enter a password to test its strength: ")
print(password_strength(user_password))
