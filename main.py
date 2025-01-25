from encryption import generate_key, load_key
from gui import add_password_gui, retrieve_password_gui, view_all_accounts_gui, generate_password_gui, export_passwords_gui
from master_password import verify_master_password  # Import the master password verification
import tkinter as tk
from tkinter import messagebox

def main():
    try:
        load_key()
    except FileNotFoundError:
        generate_key()

    # Verify master password before showing the manager
    if not verify_master_password():  # Verify the master password on startup
        messagebox.showerror("Error", "Incorrect master password!")
        return

    # GUI Setup
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("400x400")

    # Add buttons to the window
    tk.Button(root, text="Add Password", command=add_password_gui, width=20).pack(pady=10)
    tk.Button(root, text="Retrieve Password", command=retrieve_password_gui, width=20).pack(pady=10)
    tk.Button(root, text="View All Accounts", command=view_all_accounts_gui, width=20).pack(pady=10)
    tk.Button(root, text="Generate Password", command=generate_password_gui, width=20).pack(pady=10)
    tk.Button(root, text="Export Passwords", command=export_passwords_gui, width=20).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
