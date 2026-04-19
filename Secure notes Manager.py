import os

PASSWORD_FILE = "master_password.txt"

def encrypt_text(text, key):
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + key)
    return encrypted

def decrypt_text(text, key):
    decrypted = ""
    for char in text:
        decrypted += chr(ord(char) - key)
    return decrypted

def setup_password():
    if not os.path.exists(PASSWORD_FILE):
        print("\n== First Time Setup ==")
        password = input("Create your master password: ")
        file = open(PASSWORD_FILE, "w", encoding="utf-8")
        file.write(password)
        file.close()
        print("Password created successfully!")
        return password
    else:
        file = open(PASSWORD_FILE, "r", encoding="utf-8")
        saved_password = file.read()
        file.close()

        attempts = 0
        while attempts < 3:
            password = input("Enter your master password: ")
            if password == saved_password:
                print("Access granted!")
                return password
            else:
                attempts += 1
                remaining = 3 - attempts
                if remaining > 0:
                    print(f"Wrong password! {remaining} attempts left!")
                else:
                    print("Account locked! Too many wrong attempts!")
                    return None
        return None

def save_note(note, password):
    verify=input("Enter password to save note:")
    if verify!=password:
        print("Wrong password! Access denied!")
        return
    key = len(password)
    encrypted = encrypt_text(note, key)
    file = open("secure_notes.txt", "w", encoding="utf-8")
    file.write(encrypted)

    file.close()
    print("\nNote saved and encrypted successfully!")

def read_note(password):
        if not os.path.exists("secure_notes.txt"):
            print("\nNo note found!")
            return
# Again Check the Password!
        verify = input("Enter password to read note: ")
        if verify != password:
            print("Wrong password! Access denied!")
            return

        file = open("secure_notes.txt", "r", encoding="utf-8")
        encrypted = file.read()
        file.close()
        key = len(password)
        decrypted = decrypt_text(encrypted, key)
        print(f"\nYour Note:\n{decrypted}")


def main():
    print("=" * 40)
    print("SECURE NOTES MANAGER")
    print("with Encryption & Password Protection")
    print("=" * 40)

    password = setup_password()

    if password is None:
        print("Exiting for security!")
        return

    while True:
        print("\n1. Save New Note")
        print("2. Read Note")
        print("3. Exit")

        choice = input("\nChoose (1/2/3): ")

        if choice == '1':
            note = input("Enter your note: ")
            save_note(note, password)
        elif choice == '2':
            read_note(password)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


main()