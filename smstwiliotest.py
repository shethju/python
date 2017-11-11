from twilio.rest import Client

account_sid="AC1fb40c3b261055789da2b637d2bdb49e"
auth_token="e42c7ed0a71f1c360a61304035b2c400"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="hello test",
    to="+14436532199",
    from_="+16507271831")
print message.sid
    

