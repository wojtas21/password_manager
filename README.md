🔑 Password Manager

Password Manager is a simple and secure program for generating, storing, and managing passwords. All passwords are encrypted using Fernet (cryptography), and access to them is protected by a master password.

📌 Features

✅ Secure access – requires a master password to unlock stored passwords.
✅ Password generation – users can generate random passwords based on selected criteria.
✅ Password encryption – all passwords are stored in passwords.json in an encrypted format.
✅ View saved passwords – after entering the master password, users can view stored passwords.
✅ Delete passwords – allows users to remove specific passwords from the database.
✅ Change the master password – users can set a new master password at any time.
✅ Search for saved passwords – users can find stored passwords based on service names.

🛠️ Requirements
	•	Python 3.x
	•	Libraries: cryptography, bcrypt

Install required libraries:
    `pip install cryptography bcrypt`