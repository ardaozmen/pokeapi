import smtplib
from email.message import EmailMessage
from utils.poke import Pokemon
from helper.logger import logging
from helper.tools import email_parser
from helper.text_helper import TextHelper
from models.sender import Sender


class Forward(Pokemon):
    """
        This class contains smtplib handlers for E-mailing with SMTP.Gmail.

    """
    
    def __init__(self):
        self.EMAIL_ADDRESS = Sender.sender_email
        self.EMAIL_PASSWORD = Sender.sender_password
        self.poke_name = Pokemon.poke_name
        self.to_email = Pokemon.to_email
        

    def send(self):
        msg = EmailMessage()
        msg['Subject'] = 'This is my Platin Bilisim Case Study.'
        msg['From'] = self.EMAIL_ADDRESS 
        msg['To'] = self.to_email
        email_string = email_parser(self.to_email)
        msg.set_content(f'Hello {email_string}, \nAttached is your pokemon pdf.')


        with open(f'./outputs/{self.poke_name}.pdf', 'rb') as pdf:
            msg.add_attachment(pdf.read(), maintype='application', subtype='octet-stream', filename=f'{self.poke_name}.pdf')
            
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD) 
            smtp.send_message(msg)
        logging.info(TextHelper.EMAIL_SENT_SUCCESSFULLY)