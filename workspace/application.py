from flask import Flask, request
import threading
from combine import makememe
#import time

import requests

# class MyThread(threading.Thread):
#     self.names = None
#     self.msgs = None
#     def run(self):
#         makememe(self.names, self.msgs)

app = Flask(__name__)

ACCESS_TOKEN = "EAAHuZA9kshqsBAGCzxKKolyrClKWTp6Bw3dmfmB6RGNFkqyBS9QPsZCYr2g1JrmtbyljpUQoDTufc21vMW5hCebXpc2Mg2ewoHTWM70SE0wZCkW7ugIQw4UYn9ZBu4rOtSUgJWp3iIx3cZCXDO0kgtoyQsfbaRmli79lr0R9rMwZDZD"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    #print(data)
    #if len():
    #    print("no data :(")

        # {'object': 'page', 'entry': [{'id': '1814432035521430', 'time': 1512287064447, 'messaging': [{'sender': {'id': '1353761844750786'}, 'recipient': {'id': '1814432035521430'}, 'timestamp': 1512286962500, 'message': {'mid': 'mid.$cAAYowo2CA9JmTJkLRFgG1PC8uqB9', 'seq': 26923, 'text': 'David malan|i want to eat cookies', 'nlp': {'entities': {}}}}]}]}
    #    return

    try:
        sender = data['entry'][0]['messaging'][0]['sender']['id']
    except KeyError:
        print ("KEY ERROR")
        print(data)
        return "error"

    #if len(data['entry'][0]['messaging'][0]['message']) < 4:
    #    return "error: no text"

    #if len(sender) < 16:
    #    return "error"

    print(str(len(sender)))

    try:
        message = data['entry'][0]['messaging'][0]['message']['text']
    except:
        print ("MESSAGE ERROR")
        print(data)
        return "error"
    namelist = ["malan", "matrix", "ellenbama", "trump"]

    print("sender "+sender)
    print("message "+message)
    #print("namelist "+namelist)

    # Split the message from the vertical bar
    if "|" in message:
        name, msg = message.lower().split('|')
    else:
        reply(sender, "Usage: Name|Message")
        return "error"

    print(name)

    if not name in namelist:
        reply(sender, ":( :/ o_o 0_0 O_O -_- Please choose either Malan, Matrix, Trump, or Ellenbama.")
        return "error"

    if min(len(name), len(msg)) == 0:
        reply(sender, "Usage: Name|Message")
        return "error"

    # Remove special characters from message
    msgs = msg.split(" ")
    for i in range(len(msgs)):
        msgs[i] = ''.join([c for c in msgs[i] if c.isalpha() and c != '\''])

    # :( :/ o_o 0_0 O_O p_p j_j -_- +_+ x_x $_$ @_@ !_!
    reply(sender, "Your input has been received. We will have your video shortly.")

    thr = threading.Thread(target=makememe, kwargs={'voice':name, 'saythis':msgs})
    thr.start()

    #makememe(name, msgs)
    #time.sleep(30)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)