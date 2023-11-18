"""
Write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum
length set by a variable.
"""
PASSWORD_MINIMUM_LENGTH = 6
password = input("Enter password: ")
while len(password) < PASSWORD_MINIMUM_LENGTH:
    print("Invalid password, your password should contain at least 6 characters")
    password = input("Enter password: ")
print("Password: ", "*"*len(password))
