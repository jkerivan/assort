from twilio.rest import Client
import os

class TwilioMessageClient:
    def __init__(self, account_sid, auth_token, twilio_phone_number):
        self.client = Client(account_sid, auth_token)
        self.twilio_phone_number = twilio_phone_number

    def send_sms(self, to_number, message):
        message = self.client.messages.create(
            body=message,
            from_=str(self.twilio_phone_number),
            to=to_number
        )
        return message.sid
