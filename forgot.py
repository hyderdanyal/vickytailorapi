import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import math
import random
from pymongo import MongoClient


def Forgot(email):

    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor
    authentication = db.authentication

    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
        ONE = OTP
    OTP = ""
    data = {
        'otp': ONE
    }
    distinctemail = db['authentication'].distinct("email")
    if email in distinctemail:
        print('Email', email, 'OTP', ONE)
        authentication.update_one({"email": email}, {"$set": {"otp": ONE}})

        mail_content = 'Sorry to hear you forgot your password, here is your OTP: ' + ONE
        # print(mail_content)

        # The mail addresses and password
        sender_address = 'test@spm.technofiz.com'
        sender_pass = 'test@123'
        receiver_address = email
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        # The subject line
        message['Subject'] = 'Vicky Tailor forget password'
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('mail.spm.technofiz.com', 587)
        session.starttls()  # enable security
        # login with mail_id and password
        session.login(sender_address, sender_pass)
        text = message.as_string()
        print(text)

        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        return (True)
    else:
        return (False)
