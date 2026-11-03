import os
import yaml
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import getpass
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def addContact(key):
    name = input("Enter Full Name: ")
    email = input("Enter Email Adress: ")

    with open("user.yaml", "r") as f:
        data = yaml.safe_load(f)

    if ("contacts" in data):
        contacts = yaml.safe_load(decrypt(bytes.fromhex(data["contacts"]), key).decode("utf-8"))
    else:
        contacts = []

    contacts.append({"name": name, "email": email})
    data["contacts"] = encrypt(bytes(yaml.safe_dump(contacts), "utf-8"), key).hex()
    with open("user.yaml", "w") as f:
        yaml.safe_dump(data, f)

    print("Contact Added.")

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return (cipher.nonce + tag + ciphertext)

def decrypt(data, key):
    GCMnonce = data[:16]
    GCMtag = data[16:32]
    ciphertext = data[32:]

    cipher = AES.new(key, AES.MODE_GCM, nonce=GCMnonce)
    return cipher.decrypt_and_verify(ciphertext, GCMtag)

