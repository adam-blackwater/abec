class Envelope():

    def __init__(self, to, frm, subject, date, reply_to, cc, bcc, mail_id):
        self.to = to
        self.frm = frm 
        self.subject = subject
        self.date = date
        self.reply_to = reply_to
        self.cc = cc
        self.bcc = bcc
        self.mail_id = mail_id

    def out(self):
        return f'{self.to}: {self.frm}: {self.subject}: {self.date}: {self.reply_to}: {self.cc}: {self.bcc}: {self.mail_id}'

class MessageData():

    def __init__(self, body):
        self.body = body

    def out(self):
        return f'{self.body}'
