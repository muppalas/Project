import random
import string

def generate_password(length=12, use_special_chars=True, use_uppercase=True, use_lowercase=True, use_numbers=True):
    # Define character sets
    characters = ''
    
    if use_special_chars:
        characters += string.punctuation  # Special characters
    if use_uppercase:
        characters += string.ascii_uppercase  # Uppercase letters
    if use_lowercase:
        characters += string.ascii_lowercase  # Lowercase letters
    if use_numbers:
        characters += string.digits  # Numbers
    
    # If no character set is selected, use a default set of lowercase letters
    if not characters:
        characters = string.ascii_lowercase

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'

    password = generate_password(length, use_special_chars, use_uppercase, use_lowercase, use_numbers)
    print("Generated password:", password)
