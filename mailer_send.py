import os
import requests
from dotenv import load_dotenv
import base64

load_dotenv()

API_KEY = os.getenv("MAILERSEND_API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found.")

from_email = "contacto@modware.lat"
from_name = "Modware"

to_email = "paulmrg461@gmail.com"  
to_name = "Mr. Paul Realpe"

subject = "Test email"

text_content = f"""Dear {to_name},

This is a test message using MailerSend API from Python Script.

Best regards,
Paul Realpe
Software Engineer
Modware"""

html_content = f"""
<p>Dear {to_name},</p>
<p>This is a test message using MailerSend API from Python Script.</p>
<p>Best regards,<br>
<strong>Paul Realpe</strong><br>
Software Engineer<br>
<strong>Modware</strong></p>
"""

attachment_path = "image.png"

if not os.path.isfile(attachment_path):
    raise FileNotFoundError(f"El archivo {attachment_path} no fue encontrado.")

with open(attachment_path, "rb") as f:
    attachment_content = f.read()
    attachment_encoded = base64.b64encode(attachment_content).decode('utf-8')

payload = {
    "from": {
        "email": from_email,
        "name": from_name
    },
    "to": [
        {
            "email": to_email,
            "name": to_name
        }
    ],
    "subject": subject,
    "text": text_content,
    "html": html_content,
    "attachments": [
        {
            "name": os.path.basename(attachment_path),
            "data": attachment_encoded
        }
    ]
}

url = "https://api.mailersend.com/v1/email"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    print("Email sent successfully!")
    print("Response:", response.json())
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Error sending email:", err)
