from fastapi import FastAPI, Request
from twilio_mail import Email
from twilio_mail import SmsMessage

app = FastAPI()

@app.post("/")
async def read_root(request:Request):

    # Get the request body and decode from incoming byte type
    request_body = await request.body()
    request_body = request_body.decode()

    # Create the SmsMessage class with the request body
    a = SmsMessage(request_body.split("&"))
    print(request_body.body)

    # Create the Email class and call the send_email() function
    email = Email("hendry@hendryratnam.com",['hendryratnam@gmail.com'],"Testing",request_body.body)
    email.send_email()