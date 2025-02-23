from cryptography.fernet import Fernet
import random
import string
import os
import json
import bcrypt


def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(data, key):
    f = Fernet(key)
    return f.decrypt(data).decode()


def save_encrypted_passwords(passwords):
    key = load_key()
    encrypted_data = encrypt_data(json.dumps(passwords), key)
    with open("passwords.json", "wb") as f:
        f.write(encrypted_data)

def load_encrypted_passwords():
    if not os.path.exists("passwords.json"):
        return {}
    
    key = load_key()
    with open("passwords.json", "rb") as f:
        encrypted_data = f.read()
    try:
        return json.loads(decrypt_data(encrypted_data, key))
    except:
        print("Error: Could not decrypt passwords. Wrong key?")
        return {}


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

        passwords = load_encrypted_passwords()
        passwords[service] = password
        save_encrypted_passwords(passwords)

        print(f"Generated password for {service}: {password}")
        return password


def read_passwords():
    passwords = load_encrypted_passwords()
    if not passwords:
        print("No saved passwords or decryption error.")
    else:
        for service, password in passwords.items():
            print(f"{service}: {password}")


def delete_password():
    passwords = load_encrypted_passwords()
    if not passwords:
        print("No saved passwords!")
        return
    
    print("Saved passwords:")
    for service in passwords:
        print(f"- {service}")

    service_to_delete = input("Enter the service you want to delete the password for: ")

    if service_to_delete in passwords:
        del passwords[service_to_delete]
        save_encrypted_passwords(passwords)
        print(f"Password for {service_to_delete} deleted.")
    else:
        print(f"Service {service_to_delete} not found.")


def login():
    if not os.path.exists("master_password.txt"):
        print("No master password set. Please set one.")
        return False

    attempts = 3
    while attempts > 0:
        password = input("Enter master password: ")

        with open("master_password.txt", "rb") as f:
            stored_hash = f.read()

        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print("Access granted.")
            return True
        else:
            attempts -= 1
            print(f"Wrong password. {attempts} attempts left.")
    
    print("Access Denied. Too many failed attempts.")
    return False


def set_master_password():
    if os.path.exists("master_password.txt"):
        print("Master password is already set. You cannot set a new one.")
        return

    password = input("Set master password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    with open("master_password.txt", "wb") as f:
        f.write(hashed)
    print("Master password set successfully.")


def change_master_password():
    if not os.path.exists("master_password.txt"):
        print("No master password set. Please set one.")
        return
    
    password = input("Please enter your current master password:  ")
    with open("master_password.txt", "rb") as f:
        stored_hash = f.read()
    
    if not bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        print("Incorrect master password. Cannot change password.")
        return
    
    new_password = input("Enter your new master password:  ")
    new_hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    with open("master_password.txt", "wb") as f:
        f.write(new_hashed)
    print("Master password changed successfully!")


def edit_existing_password():
    passwords = load_encrypted_passwords()
    if not passwords:
        print("No saved passwords!")
        return

    print("Saved services:")
    services = list(passwords.keys())  
    for index, service in enumerate(services, start=1):
        print(f"{index}. {service}")

    choice = input("Enter the number or name of the service you want to edit: ").strip()


    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(services):
            service_name = services[choice - 1]  
        else:
            print("Invalid number selection.")
            return
    else:

        if choice in passwords:
            service_name = choice
        else:
            print("Service not found.")
            return


    new_password = input(f"Enter new password for {service_name} (or leave empty to generate one): ").strip()
    
    if not new_password:
        new_password = generate_password()


    passwords[service_name] = new_password
    save_encrypted_passwords(passwords)

    print(f"Password for {service_name} updated successfully!")
    


def menu():
    generate_key()

    if not os.path.exists("master_password.txt"):
        set_master_password()

    if not login():
        return

    while True:
        print("\nPassword Manager")
        print("1. Generate a new password")
        print("2. Show saved passwords")
        print("3. Delete a saved password")
        print("4. Exit Program")
        print("5. Change master password")
        print("6. Search for a saved password")
        
        choice = input("Choose an option (1/2/3/4/5/6):   ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            read_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            print("Exiting program")
            break
        elif choice == "5":
            change_master_password()
        elif choice == "6":
            search_passwords()
        else:
            print("Invalid choice. Select a valid option (1/2/3/4).")

menu()