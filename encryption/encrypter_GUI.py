from tkinter import *
from tkinter import filedialog
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def enable_menu():
    filemenu.entryconfig("Close", state="normal")


def disable_menu():
    filemenu.entryconfig("Close", state="disabled")


def save():
    global mainFile
    global message
    print("save")

    message = txtMessage.get("1.0", "end-1c")

    if root.fileName == "":
        root.fileName = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

    mainFile = open(root.fileName, "w")
    mainFile.write(message)

    mainFile.close()


def open_file():
    global mainFile

    print("open")
    root.fileName = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    try:
        mainFile.close()
    except:
        pass
    mainFile = open(root.fileName, "r+")
    mainText = mainFile.read()
    set_input(mainText)
    enable_menu()

    mainFile.close()


def close():
    global mainFile

    try:
        mainFile.close()
    except:
        pass

    txtMessage.delete('1.0', "end-1c")
    root.fileName = ''
    disable_menu()
    menubar.configure(state=NORMAL)


# Encrypting and Decrypting functions:
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


def encrypt_message(message_to_encrypt, provided_password):
    message = message_to_encrypt.encode()

    key = getkey(provided_password)
    f = Fernet(key)
    encrypted = f.encrypt(message)
    return encrypted


def decrypt_message(encrypted_message, provided_password):
    encrypted = encrypted_message.encode()

    key = getkey(provided_password)

    try:
        f = Fernet(key)
        decrypted = f.decrypt(encrypted)
        return decrypted.decode()
    except Exception:
        raise Exception("Incorrect Key / Decryption failed")


def encrypt_function():
    global password_entry
    global status_message
    global txtMessage

    # Encrypt message
    password_provided = password_entry.get()
    message_to_encrypt = txtMessage.get("1.0", "end-1c")

    new_message = encrypt_message(message_to_encrypt, password_provided)

    # Overwrite file
    try:
        mainFile = open(root.fileName, "wb")
        mainFile.write(new_message)
        mainFile.close()
    except FileNotFoundError:
        pass

    set_input(new_message)
    status_message.configure(text="Encryption Successful!")


def decrypt_function():
    global decrypt_password_entry
    global decrypt_status_message
    global txtMessage

    # Encrypt message
    password_provided = decrypt_password_entry.get()
    message_to_decrypt = txtMessage.get("1.0", "end-1c")

    try:
        new_message = decrypt_message(message_to_decrypt, password_provided)
    except Exception:
        decrypt_status_message.configure(text="Incorrect Key / Decryption failed")
    else:
        # Overwrite file
        try:
            mainFile = open(root.fileName, "w")
            mainFile.write(new_message)
            mainFile.close()

        except FileNotFoundError:
            pass

        set_input(new_message)

        decrypt_status_message.configure(text="Decryption Successful!")


def encrypt():
    global status_message
    global password_entry

    window = Toplevel()
    window.wm_title("Encrypt")

    title = Label(window, text="Encrypt a file", font=("Roboto", 20))
    title.grid(row=0, column=0)

    password_text = Label(window, text="Password:", font=("Roboto, 12"))
    password_text.grid(row=1, column=0)
    password_entry = Entry(window, show="*")
    password_entry.grid(row=1, column=1)
    encrypt_button = Button(window, text="Encrypt!", font=("Roboto", 12), command=encrypt_function)
    encrypt_button.grid(row=2, column=0)
    status_message = Label(window, text="", font=("Roboto", 12))
    status_message.grid(row=2, column=1)


def decrypt():
    global decrypt_password_entry
    global decrypt_status_message

    decrypt_window = Toplevel()
    decrypt_window.wm_title("Decrypt")

    title = Label(decrypt_window, text="Decrypt a file", font=("Roboto", 20))
    title.grid(row=0, column=0)

    decrypt_password_text = Label(decrypt_window, text="Password:", font=("Roboto, 12"))
    decrypt_password_text.grid(row=1, column=0)
    decrypt_password_entry = Entry(decrypt_window, show="*")
    decrypt_password_entry.grid(row=1, column=1)
    decrypt_encrypt_button = Button(decrypt_window, text="Decrypt!", font=("Roboto", 12), command=decrypt_function)
    decrypt_encrypt_button.grid(row=2, column=0)
    decrypt_status_message = Label(decrypt_window, text="", font=("Roboto", 12))
    decrypt_status_message.grid(row=2, column=1)


root = Tk()
root.title("Text editor")
root.geometry('1280x720')

root.fileName = ""

txtMessage = Text(root, width=1280, height=720)
txtMessage.grid(column=1, row=0)


def set_input(value):
    txtMessage.delete(1.0, "end-1c")
    txtMessage.insert(1.0, value)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Close", command=close, state="disabled")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

securitymenu = Menu(menubar, tearoff=0)
securitymenu.add_command(label="Encrypt", command=encrypt)
securitymenu.add_command(label="Decrypt", command=decrypt)
menubar.add_cascade(label="Security", menu=securitymenu)

root.config(menu=menubar)
menubar = Menu(root)
root.mainloop()
