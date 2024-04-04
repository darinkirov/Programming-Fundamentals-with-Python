def is_valid_password(password):
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        return False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    if sum(char.isdigit() for char in password) < 2:
        print("Password must have at least 2 digits")
        return False
    return True


password = input("Enter the password: ")
if is_valid_password(password):
    print("Password is valid")
