import random
import string

def generate_password():
    while True:

        length = input("Insert length of password: ")
        if not length.isdigit():
            print("You can't type letters in this field! Please try again!")
        else:
            length = int(length)
            print("Success")
        

        print("1. Special Characters")
        print("2. Numbers")
        print("3. Uppercase Letters")
        print("4. Lowercase Letters")
        requirements = input("Select which requirements you want to password contain (sperate them by commas!):  ")

generate_password()