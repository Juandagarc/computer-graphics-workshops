# Exercise 9: Random Password Generator
# Objective: Create a function that generates a random password with customizable length

import random
import string

def generate_password(length=8, include_uppercase=True, include_lowercase=True,
                     include_numbers=True, include_symbols=True):
    """Generates a random password with specified criteria"""
    if length < 1:
        raise ValueError("Length must be at least 1")

    characters = ""

    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not characters:
        raise ValueError("Must include at least one character type")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_secure_password(length=12):
    """Generates a secure password ensuring at least one character of each type"""
    if length < 4:
        raise ValueError("Length must be at least 4 for a secure password")

    required_characters = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
    ]

    all_characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    remaining_characters = [random.choice(all_characters) for _ in range(length - 4)]

    password_list = required_characters + remaining_characters
    random.shuffle(password_list)

    return ''.join(password_list)

def evaluate_strength(password):
    """Evaluates password strength"""
    score = 0
    criteria = []

    if len(password) >= 8:
        score += 1
        criteria.append("✓ Adequate length (8+ characters)")
    else:
        criteria.append("✗ Too short (less than 8 characters)")

    if any(c.islower() for c in password):
        score += 1
        criteria.append("✓ Contains lowercase")
    else:
        criteria.append("✗ No lowercase")

    if any(c.isupper() for c in password):
        score += 1
        criteria.append("✓ Contains uppercase")
    else:
        criteria.append("✗ No uppercase")

    if any(c.isdigit() for c in password):
        score += 1
        criteria.append("✓ Contains numbers")
    else:
        criteria.append("✗ No numbers")

    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
        criteria.append("✓ Contains symbols")
    else:
        criteria.append("✗ No symbols")

    if score <= 2:
        level = "Weak"
    elif score <= 3:
        level = "Moderate"
    elif score <= 4:
        level = "Strong"
    else:
        level = "Very Strong"

    return level, criteria, score

def password_exercise():
    """Password generator demonstration exercise"""
    print("=== PASSWORD GENERATOR ===\n")

    print("1. Basic password (8 characters):")
    password1 = generate_password(8)
    print(f"   {password1}")
    level, criteria, points = evaluate_strength(password1)
    print(f"   Strength: {level} ({points}/5)")

    print("\n2. Secure password (12 characters):")
    password2 = generate_secure_password(12)
    print(f"   {password2}")
    level, criteria, points = evaluate_strength(password2)
    print(f"   Strength: {level} ({points}/5)")

    print("\n3. Long password (16 characters):")
    password3 = generate_secure_password(16)
    print(f"   {password3}")
    level, criteria, points = evaluate_strength(password3)
    print(f"   Strength: {level} ({points}/5)")

    print("\n4. Letters and numbers only password:")
    password4 = generate_password(10, include_symbols=False)
    print(f"   {password4}")
    level, criteria, points = evaluate_strength(password4)
    print(f"   Strength: {level} ({points}/5)")

    print("\n=== DETAILED ANALYSIS OF LAST PASSWORD ===")
    for criterion in criteria:
        print(f"   {criterion}")
