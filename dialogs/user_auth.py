import json
import hashlib
import os

def load_users():
    if not os.path.exists("data/users.json"):
        return {}
    with open("data/users.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open("data/users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_password_strong(password):
    return len(password) >= 8 and any(c.isupper() for c in password) and any(not c.isalnum() for c in password)
