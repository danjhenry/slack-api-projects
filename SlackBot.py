from slackclient import SlackClient

slack_token = ""
sc = SlackClient(slack_token)
timeStamp = []
while True:
    chat = input('Enter chat: ')
    if chat == 'deleteAll':
        for time in timeStamp:
            sc.api_call(
                "chat.delete",
                channel="C054NCKDB",
                ts=time
                )
    elif chat == 'delete':
        sc.api_call(
            "chat.delete",
            channel="C054NCKDB",
            ts=timeStamp[len(timeStamp) - 1]
            )
            
    else:
        info = sc.api_call(
            "chat.postMessage",
            channel="#general_go2",
            text=chat,
            as_user = 'false',
            username='whyy',
            icon_url='https://ca.slack-edge.com/T054NCKBV-U2M226XAP-9db940ec6597-48'
            )
        timeStamp.append(info['ts'])
'''
groups = sc.api_call("groups.list")
for item in groups['groups']:
    print(item['id'], item['name'])
'''
