# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from twilio.rest import Client

# # Your Account SID from twilio.com/console
account_sid = "AC4f21b118a7db0806a15e25a80b174029"
# # Your Auth Token from twilio.com/console
auth_token  = "b63519b606517484861545ed854d0918"

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+918126159737", 
#     from_="+19362263494",
#     body="Hello from Python!")

# print(message.sid)


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['AC4f21b118a7db0806a15e25a80b174029']
# auth_token = os.environ['b63519b606517484861545ed854d0918']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Here's that picture of an owl you requested.",
                     media_url=['https://demo.twilio.com/owl.png'],
                     from_='whatsapp:+14155238886',
                     to='whatsapp:+918126159737'
                 )

print(message.sid)
