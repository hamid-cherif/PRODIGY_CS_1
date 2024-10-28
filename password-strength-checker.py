# password-strength-checker.py

import re

def check_password_strength(password):
    """
    Function to evaluate the strength of a password based on several criteria.

    Args:
    - password: The password to be evaluated.

    Returns:
    - str: Strength level of the password (Weak, Moderate, Strong).
    """
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[@$!%*?&]", password) is not None
    
    score = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])
    
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
