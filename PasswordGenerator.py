import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_char = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    lenght = int(input("Enter password length:"))

    alphabets_count = int(input("Enter alphabet count:"))
    digits_count = int(input("Enter digit count:"))
    special_character_count = int(input("Enter special charater count:"))

    characters_count = alphabets_count + digits_count + special_character_count

    if characters_count > lenght:
        print("Character total count is greater than password lenght.")
        return

    password = []

    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_character_count):
        password.append(random.choice(special_char))

    if characters_count < lenght:
        random.shuffle(characters)
        for i in range(length = characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

generate_password()

