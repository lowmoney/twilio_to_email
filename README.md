<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![GitHub stars](https://img.shields.io/github/stars/lowmoney/twilio_to_email)](https://github.com/lowmoney/twilio_to_email/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/lowmoney/twilio_to_email)](https://github.com/lowmoney/twilio_to_email/issues)
[![GitHub forks](https://img.shields.io/github/forks/lowmoney/twilio_to_email)](https://github.com/lowmoney/twilio_to_email/network)



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/lowmoney/twilio_to_email">
    <img src="twilio-logo-black.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SMS to your Email</h3>

  <p align="center">
    An easy to implement Python class that forwards your Twilio SMS to your email
    <br />
    <br />
    <a href="mailto: hendry@hendryratnam.com">Report Bug</a>
    ·
    <a href="mailto: hendry@hendryratnam.com">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Things Working](#installation)
* [Getting Started](#getting-started)
* [License](#license)



<!-- ABOUT THE PROJECT -->

# About the Project
As I was going through Zapier's most popular projects, I came across one that caught my eye. They had an application that could forward a text message to an email address using the Twilio API. Having experience with the Twilio API, I decided I'd make a similar project.

# Installation
Simply install via pip
```bash
pip install TwilioToEmail
```

<!-- GETTING STARTED -->
# Getting Started

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






<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.