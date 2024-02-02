import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email via Gmail
def send_email(receiver_email, subject, body):
    sender_email = "user@mailprovider.com"  # Replace with your Gmail address
    sender_password = "Password"  # Replace with your Gmail password
    body = 'This is a test from Python'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    print('Preparing everything to send email')
    try:
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main script
subject = "This is a subject"
body = "Body of the email."

# Replace 'your_email@gmail.com' with the actual recipient's email address
receiver_email = "user@emailprovider.com"

# Send email
send_email(receiver_email, subject, body)