# sms_app/management/commands/send_sms.py

from django.core.management.base import BaseCommand
from sms_app.utils import send_sms

class Command(BaseCommand):
    help = 'Send a single SMS message'

    def add_arguments(self, parser):
        parser.add_argument('phone_number', type=str, help='Phone number to send the SMS to')
        parser.add_argument('message', type=str, help='Message content of the SMS')

    def handle(self, *args, **kwargs):
        phone_number = kwargs['phone_number']
        message = kwargs['message']

        if send_sms(phone_number, message):
            self.stdout.write(self.style.SUCCESS(f'SMS sent successfully to {phone_number}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to send SMS to {phone_number}.'))
