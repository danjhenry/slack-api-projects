from slackclient import SlackClient

slack_token = ""
sc = SlackClient(slack_token)

while True:
    chat = input('Enter ts: ')
    print(sc.api_call(
        "chat.delete",
        channel="C054NCKDB",
        ts=chat
        ))

