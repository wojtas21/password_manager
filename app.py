import random
import string
import os

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
        service = input("For which site would you like to save this password: ")
        with open("passwords.txt", "a") as f:
            f.write(f"{service}: {password}\n")
        print(f"Generated password for {service}: {password}")
        return password

def read_passwords():
    with open("passwords.txt", "r") as f:
        print(f.read())


generate_password()