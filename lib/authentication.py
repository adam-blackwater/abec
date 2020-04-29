import oauth2 as oauth
import oauth2.clients.imap as imaplib


class Authentication():

    def __init__(self):

        self.consumer = oauth.Consumer(
                'your_consumer_key', 'your_consumer_secret'
                )
        self.token = oauth.Token(
                'your_users_3_legged_token', 'your_users_3_legged_token_secret'
                )

        self.url = 'https://mail.google.com/mail/b/your_users_email@gmail.com/imap/'

    def authenticate(self):
        conn = imaplib.IMAP4_SSL('imap.googlemail.com')
        conn.authenticate(self.url, self.consumer, self.token)
        return conn
