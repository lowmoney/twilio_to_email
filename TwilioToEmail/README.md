As I was going through Zapier's most popular projects, I came across one that caught my eye. They had an application that could forward a text message to an email address using the Twilio API. Having experience with the Twilio API, I decided I'd make a similar project.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
The only external package you need is the requests library. Also, you will need a [Twilio account](https://www.twilio.com/), and an [email](https://support.google.com/accounts/answer/6010255) that allows you to send emails.

### Quick Start
Simply import TwilioToEmail and pass the decoded Twilio body into the SmsMessage class. Then forward the message via the Email class's send_email function. Check out the example below.

```python
from TwilioToEmail import SmsMessage

sms_body = SmsMessage(Twilio.decode('utf-8').split("&"))

email = twilio_mail.Email("from_email","to_email","subject line")
email.send_email(sms_body)
```

### Some Nice Features
TwilioToEmail can also handle media messages as well. Files like images, videos, audio, and others are saved as either MP4 or JPG. If a path location is not given to the SmsMessage class then the default **home/last_four_digits_of_number** directory is used to save media files.


<!-- ROADMAP -->
## Roadmap
- [x] Allow user to parse through SMS body via a dictionary
- [ ] Add all default keys in the dictionary that Twilio API sends
- [ ] Allow user to compress media files
- [ ] Let user save info in CSV