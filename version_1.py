import hashlib


def crackHash(input):
    try:
        passFile = open("passwords.txt", "r")
    except FileNotFoundError:
        print("File not found.")

    for password in passFile:
        encoded = password.encode("utf-8")

        digest = hashlib.sha256(encoded.strip()).hexdigest()

        if digest == input:
            print(f"Password: {password}")
            return
        else:
            print("Passwords not found. Try again?")


if __name__ == "__main__":
    crackHash("8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92")
