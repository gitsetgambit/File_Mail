'''sending the mails fetched fileMail.py'''


from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
from pathlib import Path
import smtplib
import FileMail

for i in FileMail.pullout():
    message = MIMEMultipart()
    message["from"] = "Aditya kumar"
    message["to"] = i
    message["subject"] = "Aditya's Resume'"
    message.attach(MIMEText(
        "heii this is my resume please let me know on my skill related vacancies 😇", "plain"))
    Path = "C:\\Users\\hp\\Desktop\\file_mail\\ADITYA-KUMAR.pdf"
    binary_pdf = open(
        Path, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name="ADITYA-KUMAR.pdf")
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment',
                       filename="ADITYA-KUMAR.pdf")
    message.attach(payload)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("xyz", "xyz")
        smtp.send_message(message)
        print("sent...")
