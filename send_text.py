from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC4550f7f3597ee20190aa4f1af57b11a6"
auth_token = "0405b66c1e3ed38d5fa85c4305f22252"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+886988728994",
    from_="+14154841418",
    body="Hello there!")
