import email
import imaplib
import time
class mailReader:
    def __init__(self,email,password):
        """
        input your gmail and password and let us take care of the rest.
        """
        self.email = email
        self.password = password
        self.server = 'imap.gmail.com'

    def loginMail(self):
        """
        you dont have to run this command yourself.
        """
        self.mail = imaplib.IMAP4_SSL(self.server)
        self.mail.login(self.email, self.password)
        self.mail.select('inbox')

    def checkForNewEmail(self):
        """
        use this command to check for new emails sent to your gmail.
        """
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

                    mail_from = message['from']
                    mail_subject = message['subject']

                    # from its annexes to get the text
                    if message.is_multipart():
                        mail_content = ''

                        for part in message.get_payload():
                            # if the content type is text/plain
                            # we extract it
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:
                        # if the message isn't multipart, just extract it
                        mail_content = message.get_payload()

                    # and then let's show its result
                    print(f'From: {mail_from}')
                    print(f'Subject: {mail_subject}')
                    print(f'Content: {mail_content}')


mail = mailReader('ut.discretemathematics@gmail.com', 'DM99forever')
while (1):
    time.sleep(10)
    mail.checkForNewEmail()
    print('checked')