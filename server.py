from MailSender import MailSender
from MailReceiver import MailReceiver
from Mail import Mail

class server :
    def __init__(self, Email, password, attachments_path='./received_attachments/', log_path='./mails_log/') :
        self.Email = Email
        self.password = password
        self.log_path = log_path
        self.attachments_path = attachments_path
        self.sender = MailSender(Email, password)
        self.receiver = MailReceiver(Email, password, self.attachments_path)
        self.receiver.logger(self.log_path)

    def send_email(self, title, body, target, file=None) :
        m = Mail("Hey there!")
        m.set_body("I'm here ...")
        m.receiver("ut.discretemathematics@gmail.com")
        m.logger(self.log_path)
        if file != None :
            m.set_file("./SSD")

    def listen(self) :
        while True:
            g = self.receiver.get()
            m = Mail("Hey there!")
            m.set_body("fuck")
            m.receiver(g.receiver)
            self.sender.send(m,3)
            print(g.body)

s = server('ut.discretemathematics@gmail.com', 'DM99forever')
s.listen()
