import random
import string
import os
import json
import bcrypt


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
 

        if passwords:
            print("Saved passwords:")
            for service in passwords:
                print(f"- {service}")

            service_to_delete = input("Enter the service you want to delete the password for: ")

            if service_to_delete in passwords:

                del passwords[service_to_delete]
                print(f"Password for {service_to_delete} deleted.")

                with open("passwords.json", "w") as f:
                    json.dump(passwords, f, indent=4)

                print("Passwords updated successfully.")
            else:
                print(f"Service {service_to_delete} not found.")
        else:
            print("No passwords saved yet!")
    else:
        print("File 'passwords.json' doesn't exist.")


def login():
    attempts = 3
    while attempts > 0:
        password = input("Enter master password:  ")
        

        if os.path.exists("master_password.txt"):
            with open("master_password.txt", "rb") as f:
                stored_hash = f.read()
            

            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                print("Access granted.")
                return True
            else:
                attempts -= 1
                print(f"Wrong password. {attempts} attempts left.")
        else:
            print("No master password set. Please set one.")
            break

    print("Access Denied. Too many failed attempts.")
    return False

def set_master_password():
    password = input("Set master password:  ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    with open("master_password.txt", "wb") as f:
        f.write(hashed)
    print("Master password set successfully.")

def menu():
    if not login():
        return

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