import pandas as pd
import os
import sys
import warnings
warnings.simplefilter('ignore')

class MailSender :
    def __init__(self, sender, password) :
        self.sender = sender
        self.password = password
        self.log = False

    def logger(self, addr) :
        self.log_file = addr
        self.log = True

    def send(self, mail, index=-1) :
        t = mail.send(self)
        if self.log and index>0:
            df = pd.read_csv(self.log_file)
            df['send_time'][df.id==index] = t
            df['contact'][df.id==index] = mail.receiver
            df['subject'][df.id==index] = mail.title
            df.to_csv(self.log_file, index=False)
