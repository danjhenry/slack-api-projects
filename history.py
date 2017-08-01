from slackclient import SlackClient

slack_token = ""
sc = SlackClient(slack_token)

history = sc.api_call(
        "channels.history",
        channel="C054NCKDB",
        count=1
        )
print(history['messages'])
