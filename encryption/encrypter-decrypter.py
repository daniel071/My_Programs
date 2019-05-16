# Just to test functionality

import binascii
import hashlib
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from pathlib import Path


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


# Encrypting messages
def encryptmessage(message_to_encrypt, provided_password):
    message = message_to_encrypt.encode()

    key = getkey(provided_password)
    f = Fernet(key)
    encrypted = f.encrypt(message)
    return encrypted


# Decrypting messages
def decryptmessage(encrypted_message, provided_password):
    encrypted = encrypted_message

    key = getkey(provided_password)

    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    return decrypted.decode()


userInput = input("Would you like to encrypt or decrypt? (e/d) ".lower())
if userInput == "e":
    file_directory = input("Input directory of file to encrypt: ")
    file = open(file_directory, "r")
    message = file.read()
    provided_password = input("Provide password for encryption: ")
    new_message = encryptmessage(message, provided_password)

    newName = Path(file_directory).stem
    newerName = "{newName}_encrypted.txt".format(newName=newName)
    file.close()
    file = open(newerName, "wb")
    file.write(new_message)
    file.close()

    print("File encrypted successfully! File is located at {directory}".format(directory=newerName))


elif userInput == "d":
    file_directory = input("Input directory of file to decrypt: ")
    file = open(file_directory, "rb")
    encrypted_message = file.read()
    provided_password = input("Provide password for decryption: ")
    decrypted_message = decryptmessage(encrypted_message, provided_password)

    newName = Path(file_directory).stem
    newerName = "{newName}_decrypted.txt".format(newName=newName)
    finalPath = "{fileDirectory}_decrypted.txt".format(fileDirectory=file_directory, newerName=newerName)
    file.close()
    file = open(newerName, "wb")
    file.write(decrypted_message.encode())
    file.close()

    print("File decrypted successfully! File is located at {directory}".format(directory=finalPath))

else:
    print("Command not recognised")
