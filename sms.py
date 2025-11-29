import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "rukunxxx@gmail.com"
APP_PASSWORD= "shpxxxxxxxxxld"
RECEIVER = "aaxxxxxxxxx@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "HELLO FOR PYTHON.........."
msg.set_content("This email was shared by python code....")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server :
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
from twilio.rest import Client
ACCOUNT_SID ="xxxxxxx"
AUTH_TOKEN ="xxxxxxxx"
TWILIO_NUMBER= "+19279xxx309"
RECIVER_NUMBER = "+91629xxx0132"
Client = Client(ACCOUNT_SID,AUTH_TOKEN)
merssage = Client.message.create(body="hello i am aakriti" , from_ =TWILIO_NUMBER,to=RECIVER-NUMBER)