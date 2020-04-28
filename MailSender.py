import pandas as pd
import os
import sys
import warnings
warnings.simplefilter('ignore')

class MailSender :
    def __init__(self, sender, password) :
        self.sender = sender
        self.password = password

    def send(self, mail, index=-1) :
        t = mail.send(self)