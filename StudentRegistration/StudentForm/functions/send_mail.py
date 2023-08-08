from email.message import EmailMessage
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_sender = 'ritikchahar47@gmail.com'
email_password = 'wpzbcitgsopthvaq'

def send_otp(uid, name, otp):
    email_reciever = f"{uid}@cuchd.in"
    subject = f"OTP for Registration in AI Card Authentication and Student Media Project"
    emailData =f''''
    <body style="background-color: #f5f5f5; font-family: Arial, sans-serif; color: #333; text-align: center; padding: 40px;">
        <h1 style="color: #007bff; font-weight: bold;">Welcome, {name},</h1>
        <p>We are pleased to invite you to participate in the first hiring round for two exciting projects:</p>
        <ul style="list-style-type: none; padding: 0; margin-top: 20px;">
            <li style="margin-bottom: 10px;">AI Card Authentication</li>
            <li style="margin-bottom: 10px;">Student Media</li>
        </ul>
        <p>Below is your One-Time-Password for registration:</p>
        <h2 style="color: #28a745; font-size: 24px; margin-top: 30px; font-weight: bold;">Your OTP: {otp}</h2>
        <p style="color: #28a745; font-size: 24px; margin-top: 30px; font-weight: bold;">Please keep it confidential!</p>
        <p style="font-size: 18px; margin-top: 30px; color: #999;">Warm regards</p>
    </body>
    '''

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To']= email_reciever
    em['subject'] = subject
    em.attach(MIMEText(emailData, "html"))
    email_string = em.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
    
    return {"success":True}


if __name__ == "__main__":
    send_otp()