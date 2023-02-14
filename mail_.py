import smtplib
from email.message import EmailMessage
from string import Template

# smtp is used as the protocol of communication
# simple mail transfer protocol
email = EmailMessage()
email['from'] = '<Your name>'
email['to'] = '<receivers mail id>'
email['subject'] = '<Your subject>'
email.set_content('<your content or any file>')

# now for sending the mail
with smtplib.SMTP(host='smtp.gmail.com',port=587) as sm:
    sm.ehlo() #greet
    sm.starttls() # incription mechanism, connecting securely
    sm.login('<your mail id>','<app password>') # this is specifi for gmail
    sm.send_message(email)
    print('good')

