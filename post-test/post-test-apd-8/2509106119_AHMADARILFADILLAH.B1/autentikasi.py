import json, os
from data_mobil import clear

USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    else:
        # default admin
        users = {"admin": {"password": "admin123", "role": "admin"}}
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)
        return users

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register():
    clear()
    print("=== REGISTER USER BARU ===")
    users = load_users()
    username = input("Masukkan username baru: ")
    if username in users:
        print("Username sudah terdaftar!")
        input("Tekan Enter...")
        return None

    password = input("Masukkan password: ")
    users[username] = {"password": password, "role": "user"}
    save_users(users)
    print("Registrasi berhasil!")
    input("Tekan Enter...")

def login():
    clear()
    print("=== LOGIN ===")
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login berhasil!")
        input("Tekan Enter...")
        return username, users[username]["role"]
    else:
        print("Username atau password salah!")
        input("Tekan Enter...")
        return None, None

