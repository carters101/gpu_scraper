import smtplib
import table
import pandas as pd
import getpass
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import sys

sender_email = input('What address is sending the email? ')
recipient_email = input('What address is receving the email? ')
password = getpass.getpass('Sender password: ')

# Begin setting up HTML email
msg = MIMEMultipart()
msg['Subject'] = 'A GPU is in stock!'
msg['From'] = sender_email

# Email function receives DataFrame as input
def send_email(body):
    # Formats the email for HTML
    html = '''\
        <html>
            <head>
                <h2>Check the table below for more info.</h2>
            </head>
            <body>
                {0}
            </body>
        </html>
        '''.format(body.to_html())
    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(msg['From'], recipient_email, msg.as_string())
        server.quit()
        print('Email sent succesully')
