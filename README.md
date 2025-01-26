**Password Manager**

A simple and secure password manager built with Python. Follow the steps below to set up and run the program on your machine.

Prerequisites: Python 3.10 or above

Required libraries: tkinter, cryptography, and sqlite3

Install dependency using: pip install cryptography

---

**How to Run the Program**

**Step 1: Create the Database**

Run the create_database.py file to generate the passwords.db SQLite database file:
python create_database.py


**Step 2: Generate the Key**

Run the generate_key.py file to generate the key.key encryption file:
python generate_key.py


This file will be used for encrypting and decrypting your passwords.

**Step 3: Start the Program**

Run the main.py file to launch the Password Manager:
python main.py


On the first run, you will be prompted to set a master password. This password will be required to access your stored credentials in subsequent runs.

---

**Features**

**Add Passwords:** Save credentials for your accounts securely.

**Retrieve Passwords:** View stored credentials for specific accounts.

**Generate Passwords:** Generate strong passwords automatically.

**Export Passwords:** Export your passwords to a file (for backup purposes).

**Master Password Protection:** Ensures only you can access your data.

---

**Important Notes**

**Master Password:** Keep your master password safe! If you forget it, you will need to delete the key.key and passwords.db files to reset the application.

**Data Security:** The key.key file is essential for decrypting stored passwords. Losing this file will make your data inaccessible.

**Cross-Platform:** The application is compatible with Windows, macOS, and Linux.

---

Feel free to clone the repository and try it out!
