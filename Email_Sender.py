import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'mukherjee sen'
email['to'] = 'receiver@gmail.com'
email['subject'] = 'dummy mail'
email.set_content("i am a dummy mail")


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com', 'your passwords')
    smtp.send_message(email)
    print("all good")
print("all good")

