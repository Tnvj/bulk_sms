# sms_app/utils.py

from twilio.rest import Client
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()

def send_sms(phone_number, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            to=phone_number,
            from_=os.getenv('TWILIO_PHONE_NUMBER'),
            body=message
        )
        print(f'SMS sent successfully to {phone_number}')
        return True
    except Exception as e:
        print(f'Failed to send SMS to {phone_number}. Error: {str(e)}')
        return False
