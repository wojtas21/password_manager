# 🔑 Password Manager  

**Password Manager** is a secure and simple tool for generating, storing, and managing passwords. All stored passwords are **encrypted using Fernet (cryptography)**, and access to them is protected by a **master password**.  

---

## 📌 Features  

✅ **Secure access** – requires a **master password** to unlock stored passwords.  
✅ **Password generation** – allows users to generate **random passwords** based on selected criteria.  
✅ **Password encryption** – all stored passwords are **encrypted** for security.  
✅ **View saved passwords** – users can view stored passwords after authentication.  
✅ **Delete passwords** – users can remove specific passwords from the database.  
✅ **Change the master password** – allows users to set a **new master password** at any time.  
✅ **Search for saved passwords** – users can **search for stored passwords** by service name.  

---

## 🛠️ Requirements  

- **Python 3.x**  
- Required Libraries:  

  ```bash
  pip install cryptography bcrypt