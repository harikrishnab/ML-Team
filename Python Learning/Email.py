import smtplib

gmail_user = '*********@gmail.com'  
gmail_password = '***********'

sender = '**********@gmail.com'
receivers = ['*******@gmail.com']

message = """From: %sender
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
   smtpObj.ehlo()
   smtpObj.login(gmail_user, gmail_password)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except Exception:
   print ("Error: unable to send email")
