import smtplib
from pydantic import BaseModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from core.handler.st_handler import pipeline_aggregation


class Email(BaseModel):
    rec_email: str
    subject: str


def send_email(email: Email):
    sender_email = "pratihari.11priyanka@gmail.com"
    sender_password = "szytdjvpzmvcqlou"
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject
    body = pipeline_aggregation()
    body = str(body)

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.send_message(message)

        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:

        return {"message": str(e)}
