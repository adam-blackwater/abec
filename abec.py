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
                print(headers)
            M.close()
            M.logout()
    except ConnectionRefusedError as cre:
        print(cre)
    except imaplib.IMAP4.error as e:
        print(e)

    # for envelope in envelopes:
    #    print(envelope.out(), '\n')

    # for message_body in bodies:
    #    print(message_body, '\n')
    #    print(message_body.out(), '\n')


if __name__ == '__main__':
    if first_time_set_up(True):
        account = initalise_account()
        access_account(account)

           #  # envelopes = list()
           #  bodies = list()
           #  for num in data[0].split():
           #      typ, data = get_message(M, num)
           #      # mail = email.message_from_bytes(data[0][1])
           #      mail = email.message_from_bytes(data[0][1])
           #      if mail.is_multipart() is False:
           #          print(mail.get_body(preferencelist=('related', 'html', 'plain')))
           #      message_body = create_body(mail)
           #      # print(mail, '\n')
           #      # envelope = create_envelope(mail)
                # message_body = create_message_body(mail)
                # envelopes.append(envelope)
           #      bodies.append(message_body)
