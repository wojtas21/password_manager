import random
import string

def generate_password():
    while True:
        length = input("Insert length of password: ")
        if not length.isdigit():
            print("You can't type letters in this field! Please try again!")
            continue
        length = int(length)

        print("1. Special Characters")
        print("2. Numbers")
        print("3. Uppercase Letters")
        print("4. Lowercase Letters")
        requirements = input("Select which requirements you want the password to contain (separate them by commas!):  ")

        characters = ""

        if "1" in requirements:
            characters += string.punctuation
        if "2" in requirements:
            characters += string.digits
        if "3" in requirements:
            characters += string.ascii_uppercase
        if "4" in requirements:
            characters += string.ascii_lowercase

        if not characters:
            print("You must select at least one option!")
            continue

        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated password: {password}")
        return password

generate_password()