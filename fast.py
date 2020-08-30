import sqlite3
from fastapi import FastAPI, Request
from twilio_mail import Email
from twilio_mail import SmsMessage

app = FastAPI()

@app.get("/")
def root():
    return "Hello world"

@app.post("/send_to_email")
async def read_root(request:Request):

    # Get the request body and decode from incoming byte type
    request_body = await request.body()
    request_body = request_body.decode()

    # Create the SmsMessage class with the request body
    sms = SmsMessage(request_body.split("&"))
    print(sms.body)

    # Create the Email class and call the send_email() function
    email = Email("hendry@hendryratnam.com",'hendryratnam@gmail.com',"Testing")
    email.send_email(sms)