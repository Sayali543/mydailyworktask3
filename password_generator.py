import random
import string

def generate_password(length):
    """
    Generates a strong and random password of the specified length.
    Includes uppercase, lowercase, digits, and special characters.
    """
    if length < 4:
        print("Password length should be at least 4 characters for complexity.")
        return None
    
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
    
    # Fill the rest of the password length with random characters from all pools combined
    all_characters = lowercase + uppercase + digits + special_chars
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to make it more random
    random.shuffle(password)

    return ''.join(password)

def main():
    # Prompt the user to specify the desired password length
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()
