class MessagePayload():

    def __init__(self, plain_text, html):
        self.plain_text = plain_text
        self.html = html


class MessageBody():

    def __init__(self, body, headers, uid):
        self.body = body
        self.uid = uid

    def get(self):
        return self.message


class MessageData():

    def __init__(self, headers, envelope, plain_text, html):
        self.headers = headers
        self.envelope = envelope
        self.plain_text = plain_text
        self.html = html

    def get_headers(self):
        return self.headers

    def get_envelope(self):
        return self.envelope


class MessageFull():

    def __init__(self, payload):
        self.payload = payload


class Adress():

    def __init__(self, name, mailbox, host):
        self.name = name
        self.mailbox = mailbox
        self. host = host
