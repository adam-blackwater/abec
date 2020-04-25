import os
import imaplib
from models.models import Message

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')


def go():
    try:
        with imaplib.IMAP4_SSL('imap.gmail.com') as M:
            M.login(email, password)
            message = M.select()
            message = Message(message)
            M.close()
            M.logout()
            print(message.get())
    except ConnectionRefusedError as cre:
        print(cre)
    except imaplib.IMAP4.error as e:
        print(e)


if __name__ == '__main__':
    go()
