import json
import traceback
from tkinter import simpledialog, messagebox
from db_manager import connect_db
from encryption import get_fernet

# Export passwords to a JSON file
def export_passwords():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT account, username, password, notes FROM passwords")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            messagebox.showerror("Export Failed", "No passwords to export.")
            return

        passwords = []
        fernet = get_fernet()
        for row in rows:
            account, username, encrypted_password, notes = row
            try:
                decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            except Exception:
                continue  # Skip problematic rows

            passwords.append({
                "Account": account,
                "Username": username,
                "Password": decrypted_password,
                "Notes": notes
            })

        filename = simpledialog.askstring("Export Passwords", "Enter filename (e.g., passwords.json):")
        if not filename:
            return

        if not filename.endswith(".json"):
            filename += ".json"

        with open(filename, "w") as file:
            json.dump(passwords, file, indent=4)

        messagebox.showinfo("Success", f"Passwords exported to {filename} successfully!")

    except Exception as e:
        error_message = traceback.format_exc()
        with open("error_log.txt", "w") as error_file:
            error_file.write(error_message)
        messagebox.showerror("Export Failed", f"An error occurred during export.\nDetails logged to 'error_log.txt'")
