from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

mock_db = {}

def encrypt_password(password):
    return cipher_suite.encrypt(password.encode('utf-8'))

def store_user(name, email, address, username, password, role="student"):
    encrypted_password = encrypt_password(password)
    mock_db[username] = {
        'name': name,
        'email': email,
        'address': address,
        'password': encrypted_password,
        'role': role
    }

def validate_user(username, password):
    if username in mock_db:
        encrypted_password = mock_db[username]['password']
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')
        if password == decrypted_password:
            return mock_db[username]['role']

    return None