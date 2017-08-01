from slackclient import SlackClient


#slack_token = "xoxp-5158427403-89070235363-221333790775-494335af088df84f1524c8b60360baf8"
slack_token = 'xoxb-133288543732-fcfZ7i3KH9HtTTyb78ZAj0EG'
sc = SlackClient(slack_token)

while True:
    chat = input('Enter ts: ')
    print(sc.api_call(
        "chat.delete",
        channel="C054NCKDB",
        ts=chat
        ))

'''
groups = sc.api_call("groups.list")
for item in groups['groups']:
    print(item['id'], item['name'])


#    channel="G6H3YHEF8",
'''
