import random
import string

class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length):
        password = ''.join(random.choice(self.characters) for _ in range(length))
        return password

    def run(self):
        print("Welcome to the Password Generator!")
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Password length must be a positive integer.")
            else:
                generated_password = self.generate_password(password_length)
                print("Generated Password:", generated_password)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    password_generator = PasswordGenerator()
    password_generator.run()

if __name__ == "__main__":
    main()
