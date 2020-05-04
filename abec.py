import os
import email
import pprint
import imaplib
from models.account import Account
from models.models import Envelope

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
    return (typ, data)


def access_account(account):
    try:
        with imaplib.IMAP4_SSL('imap.googlemail.com') as M:
            M.login(account.email_address, account.password)
            M.select('INBOX')
            typ, data = M.search(None, 'ALL')
            envelopes = list()
            for num in data[0].split():
                typ, data = get_message(M, num)
                mail = email.message_from_bytes(data[0][1])
                frm = mail.get('from')
                subject = mail.get('subject')
                date = mail.get('date')
                reply_to = mail.get('reply')
                to = mail.get('to')
                cc = mail.get('cc')
                bcc = mail.get('bcc')
                mail_id = mail.get('message-id')
                envelope = Envelope(
                        to, frm, subject, date, reply_to, cc, bcc, mail_id
                        )
                envelopes.append(envelope)

            M.close()
            M.logout()
    except ConnectionRefusedError as cre:
        print(cre)
    except imaplib.IMAP4.error as e:
        print(e)


    for envelope in envelopes:
       print(envelope.out(), '\n')

if __name__ == '__main__':
    if first_time_set_up(True):
        account = initalise_account()
        access_account(account)
