from MailSender import MailSender
from Mail import Mail

s = MailSender('ut.discretemathematics@gmail.com', 'DM99forever')
s.logger('log.csv')

m = Mail("Hey there!")
m.set_body("I'm here ...")
m.receiver("ut.discretemathematics@gmail.com")
m.set_file("./810194321.jpg")
m.logger("./sent_log/")

s.send(m,3)