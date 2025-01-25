import sqlite3

# Connect to the database or create it
conn = sqlite3.connect("password_manager.db")

# Create a cursor object
cursor = conn.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY,
    account TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    notes TEXT
)
""")

# Commit and close the connection
conn.commit()
conn.close()
