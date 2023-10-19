import random
import string
def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

try:
     password_length = int(input("Enter the desired password length: "))
     if password_length <= 0:
          print("Password length must be a positive integer.")
     else: 
          generated_password = generate_random_password(password_length)
          print("Generated Password:", generated_password)
except ValueError:
     print("Invalid input. Please enter a valid positive integer for the password length.")
