import email


def get_headers(M, num):
    typ, data = M.fetch(num, '(RFC822)')
    message = email.message_from_bytes(data[0][1])
    headers = {}
    headers['From'] = message.get('From')
    headers['To'] = message.get('To')
    headers['Date'] = message.get('Date')
    headers['Subject'] = message.get('Subject')
    headers['Cc'] = message.get('Cc')

    return headers


def get_full(M, num):
    typ, data = M.fetch(num, '(RFC822)')
    message = email.message_from_bytes(data[0][1])
    return (typ, data)


def get_body(M, num):
    typ, data = M.fetch(num, '(UID BODY[TEXT])')
    message = email.message_from_bytes(data[0][1])
    return (typ, data)
