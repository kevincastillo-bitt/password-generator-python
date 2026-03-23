"""
PASSWORD GENERATOR
------------------
A simple console application that generates secure random passwords.
"""

import random


def generate_password(length):
    """Create a random password with the specified length."""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    
    all_characters = lowercase + uppercase + numbers + symbols
    
    password = ""
    for _ in range(length):
        password += random.choice(all_characters)
    
    return password


def get_valid_length():
    """Ask the user for a password length and validate the input."""
    while True:
        user_input = input("Enter password length (minimum 6): ")
        
        if user_input.isdigit():
            length = int(user_input)
            if length >= 6:
                return length
            print("Error: Password must be at least 6 characters.\n")
        else:
            print("Error: Please enter a valid number.\n")


def main():
    """Run the password generator program."""
    print("=" * 40)
    print("PASSWORD GENERATOR")
    print("=" * 40)
    print()
    
    password_length = get_valid_length()
    generated_password = generate_password(password_length)
    
    print()
    print("=" * 40)
    print("Password generated successfully!")
    print(f"Your password: {generated_password}")
    print(f"Length: {password_length} characters")
    print("=" * 40)


if __name__ == "__main__":
    main()
