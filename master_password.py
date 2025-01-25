from tkinter import simpledialog, messagebox
from cryptography.fernet import Fernet

# Load encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

key = load_key()
fernet = Fernet(key)

# === Master Password Management ===
def set_master_password():
    master_password = simpledialog.askstring("Set Master Password", "Enter a master password:", show="*")
    if master_password:
        encrypted_master = fernet.encrypt(master_password.encode()).decode()
        with open("master_password.key", "w") as file:
            file.write(encrypted_master)
        messagebox.showinfo("Success", "Master password set! Restart the application.")
        exit()

def verify_master_password():
    try:
        with open("master_password.key", "r") as file:
            encrypted_master = file.read()
        stored_master = fernet.decrypt(encrypted_master.encode()).decode()

        entered_password = simpledialog.askstring("Login", "Enter the master password:", show="*")
        if entered_password == stored_master:
            return True
        else:
            messagebox.showerror("Error", "Incorrect master password!")
            return False
    except FileNotFoundError:
        messagebox.showinfo("First Run", "No master password found. Set one now.")
        set_master_password()
        return False
