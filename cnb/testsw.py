import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from urllib.request import urlopen
import os

# Set up credentials
creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/gmail.send'])

# Set up email details
sender = "bhupeshdawadi1016@gmail.com"
recipient = "bhupeshdawadi12345@gmail.com"
subject = "Subject line"
body = "Email body text"
# img_url = "https://example.com/image.jpg"

# Get image data
# img_data = urlopen(img_url).read()

# Create message container
message = MIMEMultipart()
message['to'] = recipient
message['subject'] = subject

# Add body to message container
message.attach(MIMEText(body, 'html'))

# Add image to message container
# image = MIMEImage(img_data, name=os.path.basename(img_url))
# message.attach(image)

# Encode message as Base64
raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

# Send email using Gmail API
service = build('gmail', 'v1', credentials=creds)
send_message = service.users().messages().send(
    userId="me", body={'raw': raw_message}).execute()

print(F'sent message to {recipient} Message Id: {send_message["id"]}')
