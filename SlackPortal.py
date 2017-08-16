from slackclient import SlackClient
import pickle

def load_obj(name):
    try:
        with open(name + '.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return []
    
def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

slack_token = "SLACK TOKEN HERE"
sc = SlackClient(slack_token)

timeStamp = load_obj('timeStamp')

chatName = input('Enter chat name (general): ')
channels = {'general' : 'C054NCKDB'}
while True:
    chat = input('Enter chat: ')
    if chat == 'deleteAll':
        for time in timeStamp:
            sc.api_call(
                "chat.delete",
                channel=channels[chatName],
                ts=time
                )
            
    elif chat == 'delete':
        if timeStamp:
            sc.api_call(
                    "chat.delete",
                    channel=channels[chatName],
                    ts=timeStamp[len(timeStamp) - 1]
                    )
            del timeStamp[len(timeStamp) - 1]
        else:
            print('all messages deleted')
            
    elif chat == 'deleteLast':
        num = int(input('delete back how many posts?: '))
        for x in range(num):
            if timeStamp:
                sc.api_call(
                        "chat.delete",
                        channel=channels[chatName],
                        ts=timeStamp[len(timeStamp) - 1]
                        )
                del timeStamp[len(timeStamp) - 1]
            else:
                print('all messages deleted')
    else:
        info = sc.api_call(
            "chat.postMessage",
            channel=channels[chatName],
            text=chat,
            as_user = 'false',
            username='whyy',
            icon_url='https://ca.slack-edge.com/T054NCKBV-U2M226XAP-9db940ec6597-48'
            )
        timeStamp.append(info['ts'])
    save_obj(timeStamp, 'timeStamp')
