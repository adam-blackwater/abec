class MessageBody():

    def __init__(self, body, headers, uid):
        self.body = body
        self.uid = uid

    def get(self):
        return self.message


class MessageData():

    def __init__(self, headers, envelope):
        self.headers = headers
        self.envelope = envelope

    def get_headers(self):
        return self.headers

    def get_envelope(self):
        return self.envelope


class FullMessage():

    def __init__(self, message, uid):
        self.message = message
        self.uid = uid


class Adress():

    def __init__(self, name, mailbox, host):
        self.name = name
        self.mailbox = mailbox
        self. host = host
