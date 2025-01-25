from cryptography.fernet import Fernet
from encryption import generate_key, load_key

def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

# Example Usage
if __name__ == "__main__":
    generate_key()  # Run once to generate the key
    key = load_key()
    encrypted = encrypt_password("mypassword123", key)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt_password(encrypted, key))
