from tkinter import simpledialog, messagebox
from password_manager import generate_password
from db_manager import add_password, get_password, view_all_accounts
from export import export_passwords


def add_password_gui():
    account = simpledialog.askstring("Account Name", "Enter account name:")
    username = simpledialog.askstring("Username", "Enter username:")
    password = simpledialog.askstring("Password", "Enter password (leave empty to generate one):")
    notes = simpledialog.askstring("Notes", "Enter any notes (optional):")

    if not password:
        password = generate_password()
        messagebox.showinfo("Generated Password", f"Generated password: {password}")

    if account and username and password:
        add_password(account, username, password, notes)


def retrieve_password_gui():
    account = simpledialog.askstring("Retrieve Password", "Enter account name:")
    if account:
        result = get_password(account)
        if result:
            messagebox.showinfo(
                "Password Retrieved",
                f"Account: {result['Account']}\nUsername: {result['Username']}\nPassword: {result['Password']}\nNotes: {result['Notes']}"
            )
        else:
            messagebox.showerror("Error", "No account found with that name.")


def view_all_accounts_gui():
    accounts = view_all_accounts()
    accounts_str = "\n".join(accounts) if accounts else "No accounts stored."
    messagebox.showinfo("Stored Accounts", accounts_str)


def generate_password_gui():
    length = simpledialog.askinteger("Password Length", "Enter password length (default: 16):", initialvalue=16)
    if length:
        password = generate_password(length)
        messagebox.showinfo("Generated Password", f"Generated password: {password}")


def export_passwords_gui():
    export_passwords()
