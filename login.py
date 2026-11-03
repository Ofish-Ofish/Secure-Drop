import os
import yaml
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import getpass

def verifyUser():
    email = input("Enter Email Address: ")
    password = getpass.getpass("Enter Password: ")

    with open("user.yaml", "r") as f:
        data = yaml.safe_load(f)

    if (email != data["email"]):
        return

    hash = PBKDF2(password, bytes.fromhex(data["salt"]), dkLen=64, count=1000000, hmac_hash_module=SHA256)
    if (hash.hex() != data["hash"]):
        return
    return PBKDF2(password, (bytes.fromhex(data["salt"]) + b"contacts"), dkLen=32, count=1000000, hmac_hash_module=SHA256)
    
