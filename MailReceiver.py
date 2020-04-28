import email
import imaplib
import time
import os
import sys
from Mail import Mail

class MailReceiver:
    def __init__(self, receiver, password, attachments_folder='./') :
        self.receiver = receiver
        self.password = password
        self.server = 'imap.gmail.com'
        self.log = False
        self.buffer = list()
        self.attachments_folder = attachments_folder
        if attachments_folder[-1] != '/' :
            self.attachments_folder += '/'

    def loginMail(self) :
        self.mail = imaplib.IMAP4_SSL(self.server)
        self.mail.login(self.receiver, self.password)
        self.mail.select('inbox')

    def logger(self, mails_folder) :
        self.mails_folder = mails_folder
        self.log = True

    def checkForNewEmail(self) :
        self.loginMail()
        status, data = self.mail.search(None, '(UNSEEN)')
        mail_ids = []
        for block in data:
            mail_ids += block.split()
        for i in mail_ids:
            status, data = self.mail.fetch(i, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    
                    m = Mail(message['subject'])
                    m.receiver(message['from'])

                    for part in message.walk():
                        if bool(part.get_filename()):
                            fileName = self.attachments_folder+time.ctime()
                            with open(fileName, 'wb') as f :
                                f.write(part.get_payload(decode=True))
                            m.set_file(fileName)

                    mail_content = ''  
                    if message.is_multipart():
                        for part in message.get_payload():
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:
                        mail_content += message.get_payload()
                    m.set_body(mail_content)

                    if self.log :
                        m.logger(self.mails_folder)
                        m.send(self, just_record=True, received=True)

                    self.buffer.append(m)

    def get(self) :
        print()
        w = 0
        while len(self.buffer) == 0 :
            w = (w+1)%4
            time.sleep(1)
            self.checkForNewEmail()
            print('\r'+'\|/-'[w], end='')
        one = self.buffer[0]
        self.buffer = self.buffer[1:]
        return one