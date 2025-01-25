import sqlite3
from encryption import get_fernet

def connect_db():
    return sqlite3.connect("password_manager.db")

def add_password(account, username, password, notes=""):
    conn = connect_db()
    cursor = conn.cursor()
    fernet = get_fernet()
    encrypted_password = fernet.encrypt(password.encode()).decode()
    cursor.execute(
        "INSERT INTO passwords (account, username, password, notes) VALUES (?, ?, ?, ?)",
        (account, username, encrypted_password, notes),
    )
    conn.commit()
    conn.close()

def get_password(account):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, notes FROM passwords WHERE account = ?", (account,))
    result = cursor.fetchone()
    conn.close()

    if result:
        username, encrypted_password, notes = result
        fernet = get_fernet()
        decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
        return {
            "Account": account,
            "Username": username,
            "Password": decrypted_password,
            "Notes": notes,
        }
    else:
        return None

def view_all_accounts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT account FROM passwords")
    accounts = cursor.fetchall()
    conn.close()
    return [account[0] for account in accounts]
