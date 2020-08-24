import smtplib
from email.message import EmailMessage
import urllib.parse
import requests

class Email():
    def __init__(self,sender:str,receiver:[str],subject:str,body:str):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

    def send_email(self):
        try:
            msg = EmailMessage()
            msg.set_content(self.body)
            msg['Subject'] = self.subject
            msg['From'] = self.sender
            msg['To'] = self.receiver

            gmail_server = smtplib.SMTP_SSL('smtp-relay.gmail.com',465)
            gmail_server.ehlo()
            gmail_server.send_message(msg)
            gmail_server.close()
            print(f"Email was succesfully sent to {self.receiver}")
            
        except smtplib.SMTPRecipientsRefused:
            print("Receiver(s) did not receive any email. Check the email format")
            pass
        except smtplib.SMTPHeloError:
            print("the server did not reply properly")
            pass
        except smtplib.SMTPSenderRefused:
            print(f"server did not accept from adress: {self.sender}")
            pass
        except smtplib.SMTPDataError as e:
            print(f"SMTP got an unexpected error: {e}")
            pass
        except Exception as e:
            print(f"unexpected error: {e}")
            pass

class SmsMessage():
    def __init__(self,request_body:[str],path:str=None):
        self.to_country:str
        self.to_state:str
        self.sms_message_sid:str
        self.num_media:str
        self.to_city:str
        self.from_zip:str
        self.sms_sid:str
        self.from_state:str
        self.from_city:str
        self.body:str
        self.from_country:str
        self.to_number:str
        self.to_zip:str
        self.num_segments:str
        self.message_sid:str
        self.account_sid:str
        self.from_number:str
        self.media_urls:[str]
        self.sms_status:str

        for i in request_body:
            if "ToCountry" in i:
                self.to_country = i.split("=")[1]
            if "ToState" in i:
                self.to_state = i.split("=")[1]
            if "SmsMessageSid" in i:
                self.sms_message_sid = i.split("=")[1]
            if "NumMedia" in i:
                self.num_media = i.split("=")[1]
            if "ToCity" in i:
                self.to_city = i.split("=")[1]
            if "FromZip" in i:
                self.from_zip = i.split("=")[1]
            if "SmsSid" in i:
                self.sms_sid = i.split("=")[1]
            if "FromState" in i:
                self.from_state = i.split("=")[1]
            if "SmsStatus" in i:
                self.sms_status = i.split("=")[1]
            if "FromCity" in i:
                self.from_city = i.split("=")[1]
            if "Body" in i:
                self.body = urllib.parse.unquote_plus(i.split("=")[1])
            if "To" in i:
                self.to_number = i.split("=")[1]
            if "MediaUrl" in i:
                cleaned_body = urllib.parse.unquote(i.split("=")[1])
                self.media_urls.push(cleaned_body)
            if "ToZip" in i:
                self.to_zip = i.split("=")[1]
            if "NumSegments" in i:
                self.num_segments = i.split("=")[1]
            if "MessageSid" in i:
                self.message_sid = i.split("=")[1]
            if "AccountSid" in i:
                self.account_sid = i.split("=")[1]
            if "From" in i:
                self.from_number = i.split("=")[1]

        # if len(self.media_urls) != 0: