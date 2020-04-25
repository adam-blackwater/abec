import pprint
import os
import imaplib
from models.account import Account

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')


def first_time_set_up(ans):
    if ans:
        return True
    return False


def initalise_account():
    return Account(email, email, password)


def get_message(M, num):
    typ, data = M.fetch(num, '(RFC822)')
    return data


def access_account(account):
    pp = pprint.PrettyPrinter(indent=4)
    try:
        with imaplib.IMAP4_SSL('imap.googlemail.com') as M:
            print(M.login(account.email, account.password))
            print(M.select('INBOX'))
            pp.pprint(M.list())
            data, typ = M.search(None, 'ALL')
            for num in typ[0].split():
                data = get_message(M, num)
                print('Message %s\n%s\n' % (num, data[0][1]))
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
