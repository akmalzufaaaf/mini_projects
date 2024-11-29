# Make a python program that allows user to send plain-text email from python code(?)

# import module that needed to build this program
import smtplib    # connect to smtp(simple mail transport protocol) server
import ssl   # to make a secure connection (make context, the colection of security settings to create an secure connection (TLS/SSL))
from pwinput import pwinput # make a mask when user input their password

# store all of the needed part
smtp_server = "smtp.gmail.com"
port = 465
sender_email = "codelearner360@gmail.com"
password = pwinput(prompt="Enter your password: ")
receiver_email = "akmalrahman295@gmail.com"

# create a context
context = ssl.create_default_context()

# create plain text message
message = """\
Subject: This is email from python

Hi there..
if you receive this email, that means your succesfully create a program that can make you able to send a plain-text email via python..
Congratullations!! :)

Keep it up..
you did great dude
and you even can or able to do something bigger than this:)

Bismillahirrohmannirrohim..
Semangatt:)"""

# create a secure connectin use smtplip.SMTP_SSL()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
  try:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent")
  except Exception as e:
    print(e)
