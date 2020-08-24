from typing import Optional
from fastapi import FastAPI, Request
import twilio_mail
import urllib.parse

app = FastAPI()

@app.post("/")
async def read_root(request:Request):
    a = await request.body()
    a = a.decode()
    # urllib.parse.unquote_plus(request_body[10].split("=")[1])
    for i in a.split("&"):
        print(i)
    a = twilio_mail.SMS_message(a.split("&"))
    print(a.body)

    email = twilio_mail.Email("hendry@hendryratnam.com",['hendryratnam@gmail.com'],"Testing",a.body)
    email.send_email()