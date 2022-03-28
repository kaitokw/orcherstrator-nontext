from flask import Flask, request
from linebot.models import *
from linebot import *

app = Flask(__name__)

line_bot_api = LineBotApi('F7p77Oy6+pQ7D3zh+dJv1hHWg2Fh2FmRnrRneZoz6OP1e1PFk/F0Wv0jYOAhx7hpF63nOuFCNnFaqavShreVny/b1g5+CAOksfaNSj6ES4ZTA20cXL/xUlWRDq+Oa2zW40IPhJ+qeEwhpOjBrG74KQdB04t89/1O/w1cDnyilFU=') 
handler = WebhookHandler('e6ea97c51a6f6442cfe60ef0241e3d0c')

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    reply(intent,text,reply_token,id,disname)

    return 'OK'


def reply(intent,text,reply_token,id,disname):
    if intent == 'intent 5':
        text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        line_bot_api.reply_message(reply_token,text_message)

if __name__ == "__main__":
    app.run()
