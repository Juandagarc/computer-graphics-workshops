# Exercise 7: Parentheses Validation
# Objective: Write a function that validates if a string of parentheses is balanced

def validate_parentheses(string):
    """Validates if a string of parentheses is balanced"""
    counter = 0

    for character in string:
        if character == '(':
            counter += 1
        elif character == ')':
            counter -= 1
            if counter < 0:
                return False

    return counter == 0

def parentheses_exercise():
    """Parentheses validation demonstration exercise"""
    test_cases = [
        "()",
        "(())",
        "((()))",
        "()())",
        "(()",
        ")(",
        "()()()",
        "(()(()))"
    ]

    print("Parentheses validation:")
    for case in test_cases:
        result = validate_parentheses(case)
        status = "✓ Balanced" if result else "✗ Not balanced"
        print(f"'{case}' → {status}")
