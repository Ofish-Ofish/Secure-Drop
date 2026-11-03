import os
import yaml
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import getpass


def userExist():
    with open("user.yaml", "r") as f:
        data = yaml.safe_load(f)

    if isinstance(data, dict):
        if "full_name" in data and "email" in data and "hash" in data:
            return True

    return False

def createUser():
    fullName = input("Enter Full Name: ")
    email = input("Enter Email Address: ")
    password = getpass.getpass("Enter Password: ")
    password2 = getpass.getpass("Re-enter Password: ")

    if (password != password2):
        print()
        print("Passwords do not match")
        print("Failed to register user")
        print("Exiting SecureDrop.")
        return False

    userData = {
        "full_name": fullName,
        "email": email,
    }

    userData = userData | create_salted_hash(password)

    with open("user.yaml", "w") as f:
        yaml.safe_dump(userData, f)

    print()
    print("Passwords Match.")
    print("User Registered.")
    print("Exiting SecureDrop")

    return True

def create_salted_hash(password):
    salt = get_random_bytes(16)
    hash = PBKDF2(password, salt, dkLen=64, count=1000000, hmac_hash_module=SHA256)
    dictionary = {"salt": salt.hex(), "hash": hash.hex()}
    return dictionary