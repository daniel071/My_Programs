import imaplib
from myInfo import *
import email
import sqlite3


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS news(message_date TEXT, message_from TEXT, message_subject TEXT)')
    conn.commit()


def log(message_date, message_from, message_subject):
    c.execute("INSERT INTO news (message_date, message_from, message_subject) VALUES (?, ?, ?)",
              (message_date, message_from, message_subject))
    conn.commit()


conn = sqlite3.connect('news.db')
c = conn.cursor()

create_table()
imap_host = 'imap.gmail.com'
imap_user = get_email()
imap_pass = get_password()

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

# login to server
imap.login(imap_user, imap_pass)

imap.select('hoppers_news', readonly=True)

tmp, data = imap.search(None, 'ALL')
c.execute("DELETE FROM news;")
conn.commit()
for num in data[0].split():
    typ, data = imap.fetch(num, '(RFC822)')

    raw_email = data[0][1].decode()
    email_message = email.message_from_string(raw_email)
    print(email_message['Subject'])
    print(email_message['date'])
    log(email_message['date'], email_message['From'], email_message['Subject'])

print("Logging Complete")
imap.close()
