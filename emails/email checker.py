from phue import Bridge
import imaplib
import re
import time
from myInfo import getHueIP
from myInfo import getEmail
from myInfo import getCode

print("Attempting to connect to hue")
b = Bridge(getHueIP())

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

print("Connected to hue")


imapServer = "imap.gmail.com"
port = "993"
username = getEmail()
password = getCode()

def alertLamp():
    oldHue = b.get_light(2, 'hue')
    loop = 0
    while loop <= 1:
        print(loop)
        b.set_light(2, "hue", 30202, transitiontime=2)
        time.sleep(0.5)
        b.set_light(2, "hue", oldHue, transitiontime=2)
        time.sleep(0.5)
        loop = loop + 1

    b.set_light(2, "hue", oldHue, transitiontime=2)
    time.sleep(2)

checkIntevaral = 2


Mailbox = imaplib.IMAP4_SSL(imapServer, port)
rc, resp = Mailbox.login(username, password)
if rc == 'OK':
    print("Connected to mail-server " + imapServer)
    rc, message = Mailbox.status('INBOX', "(UNSEEN)")
    unreadCount = int(re.search("UNSEEN (\d+)", str(message[0])).group(1))
    oldValue = 0
    file = open("D:/Git/Darrot-OS/My_python_programs/emails/tmp/mailnotify.tmp", "w+")
    file.write(str(unreadCount))
    file.close()
    while 1:
        rc, message = Mailbox.status('INBOX', "(UNSEEN)")
        unreadCount = int(re.search("UNSEEN (\d+)", str(message[0])).group(1))
        file = open("D:/Git/Darrot-OS/My_python_programs/emails/tmp/mailnotify.tmp", "r+")
        oldValue = int(file.readline())
        file.close()
        if unreadCount > oldValue:
            print("You got a new notification!")

            alertLamp()


        if oldValue != unreadCount:
            file = open("D:/Git/Darrot-OS/My_python_programs/emails/tmp/mailnotify.tmp", "w+")
            file.write(str(unreadCount))
            file.close()
        time.sleep(checkIntevaral)
else:
    print('Fail to connect')
Mailbox.logout()
