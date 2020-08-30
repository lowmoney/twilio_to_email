import smtplib
import csv
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import urllib.parse
import requests

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
        self.media_urls = {}
        self.sms_status:str
        self.media_types = {}
        
        self.img_paths = []

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
                self.media_urls[i.split("=")[0]] = urllib.parse.unquote(i.split("=")[1])
                # cleaned_body = urllib.parse.unquote(i.split("=")[1])
                # self.media_urls.append(cleaned_body)
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
                self.from_number = urllib.parse.unquote_plus(self.from_number)
            if "MediaContentType" in i:
                self.media_types[i.split("=")[0]] = i.split("=")[1]
                # self.media_types.append(i)
                # if 'video' in i.split('=')[1]:
                #     self.media_types = 'video'
                # else:
                #     self.media_types = 'img'

        # print(self)

        if len(self.media_urls) != 0:
            x = 0
            from_number = self.from_number.split("=")[1]
            from_number = urllib.parse.unquote_plus(from_number)
            from_number = from_number[8:]
            if path is None:
                path_to_file:str = ""
                current_home_dir = str(Path.home())
                while x<len(self.media_urls):
                    media_type = "MediaContentType{}".format(x)
                    print(media_type)
                    img_url = "MediaUrl{}".format(x)

                    if media_type in self.media_types:
                        media_type = self.media_types[media_type]

                    if img_url in self.media_urls:
                        img_url = self.media_urls[img_url]

                    img_url = urllib.parse.unquote_plus(img_url)
                    print(f"media type: {media_type}")
                    if 'video' in media_type or 'audio' in media_type:
                        path_to_file = current_home_dir + str(from_number) + "/" + self.sms_message_sid + str(x) + ".mp4"
                    if 'image' in media_type:
                        path_to_file = current_home_dir + str(from_number) + "/" + self.sms_message_sid + str(x) + ".jpg"
                    
                    self.img_paths.append(path_to_file)
                    print(f"path to file is: {path_to_file}")
                    f = open(path_to_file,'wb')
                    f.write(requests.get(img_url).content)
                    f.close()
                    x+= 1

            else:
                path_to_file:str = ""
                while x<len(self.media_urls):
                    media_type = "MediaContentType{}".format(x)
                    print(media_type)
                    img_url = "MediaUrl{}".format(x)

                    if media_type in self.media_types:
                        media_type = self.media_types[media_type]

                    if img_url in self.media_urls:
                        img_url = self.media_urls[img_url]

                    img_url = urllib.parse.unquote_plus(img_url)

                    if 'video' in media_type:
                        path_to_file = path + str(from_number) + "/" + self.sms_message_sid + str(x) + ".mp4"
                    if 'img' in media_type:
                        path_to_file = path + str(from_number) + "/" + self.sms_message_sid + str(x) + ".jpg"
                    
                    self.img_paths.append(path_to_file)
                    f = open(path_to_file,'wb')
                    f.write(requests.get(img_url).content)
                    f.close()
                    x+= 1


            # if path is None:
            #     current_home_dir = str(Path.home())
            #     for i in self.media_urls:
            #         if self.media_types == 'video':
            #             path_to_img = current_home_dir + self.to_number + "/" + self.sms_message_sid + str(x) + ".mp4"
            #         else:
            #             path_to_img = current_home_dir + self.to_number + "/" + self.sms_message_sid + str(x) + ".jpg"
            #         # path_to_img = f"{current_home_dir}/{self.to_number}/{self.sms_message_sid+str(x)}.jpg"
            #         self.img_paths.append(path_to_img)

            #         f = open(path_to_img,'wb')
            #         f.write(requests.get(i).content)
            #         f.close()
            #         x +=1
            # else:
            #     for i in self.media_urls:
            #         path_to_img = path + self.to_number + "/" + self.sms_message_sid + str(x) + ".jpg"
            #         self.img_paths.append(path_to_img)

            #         f = open(path_to_img,'wb')
            #         f.write(requests.get(i).content)
            #         f.close()
            #         x +=1

class Email():
    def __init__(self,sender:str,receiver:str,subject:str):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject

    def send_email(self,sms_message:SmsMessage):
        try:
            msg = MIMEMultipart()
            msg['Subject'] = self.subject
            msg['From'] = self.sender
            msg['To'] = self.receiver
            msg.attach(MIMEText(sms_message.body,'plain'))

            if len(sms_message.img_paths) != 0:
                for i in sms_message.img_paths:
                    attachment = MIMEApplication(open(i, "rb").read(), _subtype="txt")
                    attachment.add_header('Content-Disposition', "attachment", filename= i) 
                    msg.attach(attachment)


            gmail_server = smtplib.SMTP_SSL('smtp-relay.gmail.com',465)
            gmail_server.ehlo()
            gmail_server.sendmail(self.sender, self.receiver,msg.as_string())
            gmail_server.close()
            print(f"Email was succesfully sent to {self.receiver}")
            
        except smtplib.SMTPRecipientsRefused:
            print("When sending the email, the receiver(s) did not receive any email. Check the email format")
            pass
        except smtplib.SMTPHeloError:
            print("When sending the email, the server did not reply properly")
            pass
        except smtplib.SMTPSenderRefused:
            print(f"When sending the email, server did not accept from adress: {self.sender}")
            pass
        except smtplib.SMTPDataError as e:
            print(f"When sending the email, SMTP got an unexpected error: {e}")
            pass
        except Exception as e:
            print(f"When sending the email, an unexpected error occured: {e}")
            pass

class Csv():
    def __init__(self,filename=None):
        self.fields = ['from','message','path']
        self.filename = filename

        if filename is None:
            self.filename = "twillio.csv"
        
            with open(filename,'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(self.fields)
        else:
            with open(self.filename,'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(self.fields)


    def add_to_csv_file(self,sms_message:SmsMessage, filename=None):
        rows = [[sms_message.from_number, sms_message.body, sms_message.img_paths]]

        with open(self.filename,'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)