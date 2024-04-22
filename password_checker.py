import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Password should contain at least one lowercase letter."

    # Check for numbers
    if not re.search("[0-9]", password):
        return "Password should contain at least one number."

    # Check for special characters
    if not re.search("[!@#$%^&*()_+=\-{}[\]:;<>,.?/~]", password):
        return "Password should contain at least one special character."

    return "Password is strong."

if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)
