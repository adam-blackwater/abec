import os
import email
import pprint
import imaplib
from models.account import Account
from models.models import MessageData

email_address = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')


def first_time_set_up(ans):
    if ans:
        return True
    return False


def initalise_account():
    return Account(email_address, email_address, password)


def get_message(M, num):
    typ, data = M.fetch(num, '(RFC822)')
    mail = data[0][1].decode('utf-8')
    return (typ, mail)


def access_account(account):
    pp = pprint.PrettyPrinter(indent=4)
    try:
        with imaplib.IMAP4_SSL('imap.googlemail.com') as M:
            print(M.login(account.email_address, account.password))
            print(M.select('INBOX'))
            pp.pprint(M.list())
            typ, data = M.search(None, 'ALL')
            for num in data[0].split():
                typ, mail = get_message(M, num)
                print(typ, mail)

            print(M.close())
            print(M.logout())
    except ConnectionRefusedError as cre:
        print(cre)
    except imaplib.IMAP4.error as e:
        print(e)


if __name__ == '__main__':
    if first_time_set_up(True):
        account = initalise_account()
        access_account(account)
