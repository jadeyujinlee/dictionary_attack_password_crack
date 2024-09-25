import hashlib


def create_pass(text_file, variation_file):
    with open(text_file, "r") as f:
        passwords = f.read().split()

    with open(variation_file, "r") as p:
        variations = p.read().split()

    hashed_possibilities = {}
    for password in passwords:
        for variation in variations:
            possible_pass = password + variation
            hashed_possible_pass = hashlib.sha256(possible_pass.encode()).hexdigest()
            hashed_possibilities.update({hashed_possible_pass: possible_pass})

    return hashed_possibilities


if __name__ == "__main__":
    dictionary = create_pass("passwords.txt", "pass_variations.txt")
    password = "069f57dae98079b842a956e41d081e76487591a2ad65fa7a450717c1ab19767f"
    if password in dictionary:
        value = dictionary.get(password)
        print(f"Password found: {value}")
