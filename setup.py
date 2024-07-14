import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP serverini sozlash
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = '@gmail.com'
smtp_password = 'your-email-password'

# Elektron pochta tarkibi
sender_email = 'your-email@gmail.com'
receiver_email = 'recipient@example.com'
subject = 'Test email from Python'
body = 'This is a test email sent from Python.'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    # SMTP serveriga ulanish
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    
    # Xabarni yuborish
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
    
    # Ulanishni yopish
    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")
