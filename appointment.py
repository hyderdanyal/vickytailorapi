import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def feedback(fname, lname, email, phone, service, address, city, message):
    mail_content = '\nFirstName: ' + fname + '\nLastName: ' + lname + '\nEmail: '+email + '\nPhone:' + \
        phone + '\nService'+service + '\nAddress' + \
        address + '\nCity' + city + '\nMessage: ' + message
    # print(mail_content)

    # The mail addresses and password
    sender_address = 'test@spm.technofiz.com'
    sender_pass = 'test@123'
    receiver_address = 'hyderdanyal123@gmail.com'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    # The subject line
    message['Subject'] = 'Appointment recieved from Vicky Tailor'
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('mail.spm.technofiz.com',
                           587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    # print(text)
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
