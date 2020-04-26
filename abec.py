import pprint
import os
import imaplib
from models.account import Account
from models.models import MessageData

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')


def first_time_set_up(ans):
    if ans:
        return True
    return False


def initalise_account():
    return Account(email, email, password)


def build_message_parts(M, num):
    # typ, data = M.fetch(num, '(RFC822)')
    typ, envelope = M.fetch(num, 'ENVELOPE')
    message_data = MessageData('x', envelope[0].decode('utf-8').split(' '))
    return (typ, message_data)


def access_account(account):
    pp = pprint.PrettyPrinter(indent=4)
    try:
        with imaplib.IMAP4_SSL('imap.googlemail.com') as M:
            print(M.login(account.email, account.password))
            print(M.select('INBOX'))
            pp.pprint(M.list())
            typ, data = M.search(None, 'ALL')
            for num in data[0].split():
                typ, message_data = build_message_parts(M, num)
                # print('Message %s - %s\n%s\n' % (typ, num, data[0]))
                print(message_data.get_envelope()[9], '\n')
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
