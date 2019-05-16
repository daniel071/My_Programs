# Just to test functionality

import binascii
import hashlib
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Gather key from password input


def getkey(password_provided):
    password = password_provided.encode()  # Convert to type bytes
    salt = b"b?FJEIOEJ$^#*$#)#*R$jkfb38e0dwJIAHUYi39fj9Uk3u39320"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


# publicKey = getkey(input("Input password: "))


print("------- \nEncrypting a Message:\n")

# Encrypting messages
message_string = input("Input your message to encrypt: ")
message = message_string.encode()

publicKey = getkey(input("Input password to encrypt: "))
f = Fernet(publicKey)
encrypted = f.encrypt(message)


print("Your encrypted message is: {message}"
      .format(message=encrypted.decode()))


print("------- \nDecrypting a Message:\n")

# Decrypting messages
encrypted = input("Input encrypted message: ").encode()

publicKey = getkey(input("Input password to decrypt: "))

f = Fernet(publicKey)
decrypted = f.decrypt(encrypted)
print(decrypted.decode())
