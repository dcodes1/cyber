import random
import string

def generate_password(name, purpose, length, use_uppercase, use_lowercase, use_symbols, use_numbers):
    # Convert name to lowercase and remove spaces
    name = name.lower().replace(" ", "")

    # Define character sets based on selected options
    character_set = []
    if use_uppercase:
        character_set.extend(string.ascii_uppercase)
    if use_lowercase:
        character_set.extend(string.ascii_lowercase)
    if use_symbols:
        character_set.extend(string.punctuation)
    if use_numbers:
        character_set.extend(string.digits)

    # Shuffle the character set
    random.shuffle(character_set)

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length - len(name) - len(purpose)))
    password = name + password + purpose

    return password

# Get user inputs
name = input("Enter your name: ")
purpose = input("Enter the purpose for the password: ")
length = int(input("Enter the desired length of the password: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"

# Generate the password
password = generate_password(name, purpose, length, use_uppercase, use_lowercase, use_symbols, use_numbers)

# Display the generated password
print("Generated Password:", password)
