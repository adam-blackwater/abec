import os
import imaplib
from models.account import Account
from models.models import Envelope, MessageData
import imap.fetch as fetch

email_address = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')


def first_time_set_up(ans):
    if ans:
        return True
    return False


def initalise_account():
    return Account(email_address, email_address, password)


def create_envelope(mail):
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
    return envelope


def create_body(mail):
    body = mail.get('text')
    return body


def create_message_body(mail):
    body = mail.get('plain')
    message_body = MessageData(body)
    return message_body


def access_account(account):
    try:
        with imaplib.IMAP4_SSL('imap.googlemail.com') as M:
            M.login(account.email_address, account.password)
            M.select('INBOX')
            typ, data = M.search(None, 'ALL')
            for mail in data[0].split():
                headers = fetch.get_headers(M, mail)
                body = fetch.get_body(M, mail)
                print(headers)
                print(body)
            M.close()
            M.logout()
    except ConnectionRefusedError as cre:
        print(cre)
    except imaplib.IMAP4.error as e:
        print(e)


if __name__ == '__main__':
    if first_time_set_up(True):
        account = initalise_account()
        access_account(account)
