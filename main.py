import sqlite3
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from twilio_mail import Email
from twilio_mail import SmsMessage

conn = sqlite3.connect('examples.db')

app = FastAPI()


class user_sms_request(BaseModel):
    from_number:str
    to_email:str

class user_sms_response(BaseModel):
    from_number:str
    to_email:str

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

    response = [{"from_number":"None"},{"send_to":"None"}]
    try:
        c = conn.cursor()
        c.execute('SELECT * FROM twilio WHERE from_number=?',(sms.from_number,))
        person = c.fetchone()

        if person is not None:
            email = Email("hendry@hendryratnam@gmail.com",person[1],'Twilio to email')
            email.send_email(sms)
            response = [{"from_number":person[0]},{"send_to":person[1]}]
    except Exception as e:
        print(f"not accounted error: {e}")

    return response
            
    # print(sms.body)

    # Create the Email class and call the send_email() function
    # email = Email("hendry@hendryratnam.com",'hendryratnam@gmail.com',"Testing")
    # email.send_email(sms)

@app.post("/set_example")
def set_user(user_sms:user_sms_request,request:Request):
    try:
        c = conn.cursor()
        c.execute('INSERT INTO twilio VALUES(?,?)',(user_sms.from_number,user_sms.to_email,))
        print(user_sms.to_email)
    except sqlite3.ProgrammingError:
        print("Programming error, table not found or syntax error in SQL statement")
        pass
    except sqlite3.DatabaseError as e:
        print(f"database error occured: {e}")
    except Exception as e:
        print(f"unexpected error occured: {e}")
    
    return user_sms