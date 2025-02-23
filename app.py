import random
import string
import os
import json

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

        if os.path.exists("passwords.json"):
            with open("passwords.json", "r") as f:
                passwords = json.load(f)
        else:
            passwords = {}

        passwords[service] = password

        with open("passwords.json", "w") as f:
            json.dump(passwords, f, indent=4)

        print(f"Generated password for {service}: {password}")
        return password

def read_passwords():
    if not os.path.exists("passwords.json"):
        print("No passwords saved yet!")
        return
    
    with open("passwords.json", "r") as f:
        passwords = json.load(f)
        if not passwords:
            print("No passwords saved yet!")
        else:
            for service, password in passwords.items():
                print(f"{service}: {password}")


def delete_password():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
        print(passwords) # test
    else:
        print("File 'passwords.json' doesn't exist.")

    
    


def menu():
    while True:
        print("\nPassword Manager")
        print("1. Generate a new password")
        print("2. Show saved passwords")
        print("3. Delete a saved password")
        print("4. Exit Program")
        
        choice = input("Choose an option (1/2/3/4):   ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            read_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Select a valid option (1/2/3/4).")

menu()