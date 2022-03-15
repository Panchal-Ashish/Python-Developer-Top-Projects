import requests
from flight_data import *
from twilio.rest import Client
import smtplib

my_email = "job.ashish28@gmail.com"
password = "Ashish_28"

TWILIO_ACC_ID = "AC2859004428bce7afcad28175bb8e4d98"
TWILIO_AUTH_TOKEN = "cbcb1221265a2c170eec585158537556"
TWILIO_FROM_NUMBER = "+17082942621"
TWILIO_TO_NUMBER = '+917506058102'

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)

    def send_sms(self,message):
        self.client.messages.create(body= message, from_= TWILIO_FROM_NUMBER, to= TWILIO_TO_NUMBER)

    def send_email(self,message,google_link,to_emails):
        for email in to_emails:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:

                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"subject: Cheap Flights Available!!!\n\n{message}\n{google_link}")