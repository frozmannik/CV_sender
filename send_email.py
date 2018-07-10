
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path as op


# working fine 
def send_CV(email_send, title):  # email, title/position
    email_user = 'ADD YOUR EMAIL ADDRESS HERE'
    email_password = 'ADD YOUR PASSWORD HERE'

    subject = 'DO NOT REPLY THIS EMAIL + {}'.format(title)

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # testing

    body = 'Hi, I apologize for the spam, using your address in testing reasons. Do not reply this email.   \n TITLE : {} \n P.s if you are looking for talanted Junior software developer please reply on this email \n'.format(title)
    #body = "I saw an open position and I’m interested in applying for the {}. Attach is my CV. As you can see, I’m a recent university graduate with experience in software development and public service. I have a wide range of experience in collecting and analyzing data, developing IT solutions, also skilled in the use of Microsoft office products, like Word, Excel, PowerPoint etc. Recently, I worked in the Public sector in Russia, did an internship in a software development company and currently doing freelance. I hope you will consider me for an interview. Please feel free to contact me at n.gubenkov@gmail.com \n Thank you for your time and consideration, \n Nikita \n".format(title)
    msg.attach(MIMEText(body))

    #path = 'CV Gubenkov Nikita.docx'
    path = 'test_file.jpeg'

    part = MIMEBase('application', "octet-stream")
    with open(path, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="{}"'.format(op.basename(path)))
    msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

send_CV('frozmanik@gmail.com','Software developer')
