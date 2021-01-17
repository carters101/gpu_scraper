import smtplib, ssl
import table
import pandas as pd
import getpass

sender_email = input('What address is sending the email? ')
recipient_email = input('What address is receving the email? ')
password = getpass.getpass('Sender password: ')
message = '''\
Subject: A GPU is in stock!

It looks like some GPUs meet your criteria! Check them out below.\n'''

# Create SSL context
context = ssl.create_default_context()

# Email function receives DataFrame as input
def send_email(body):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message + body)
