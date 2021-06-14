from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ULixHg+aXBneZQZy8uWCoW9chb2jmNLZGMCZuFCUYO7fWAWY0pBZWQcn/qOsGlpyOrQLWFHfv5eN1oxLbUotgCOsTd2b3LYpNDC25G+jG2kKRsQHzeruy+UI4/f2YyHBGSwvS7rsWH0icHUHLoNSdgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f44f95adb7814ef55f175754d62fde55')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

import feedparser
weather_feed=feedparser.parse('https://www.cwb.gov.tw/rss/forecast/36_01.xml')

print(weather_feed.entries[1].title)
print(weather_feed.entries[1].description)
print(weather_feed.entries[1].link)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '你好' in msg or 'Hi' == msg or '哈嘍' == msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='你好，很高興認識你( •̀ ω •́ )✧'))
        return
    if '掰掰' in msg or '再見' == msg or 'Bye' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='掰掰🖐'))
    if '無聊' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='那就......去睡覺吧？'))
    if '自我介紹' in msg:
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='你好，我是耍廢機器人(因為我不知道名稱要打什麼，所以這名稱就誕生了！)'))
    if '早安' in msg or '午安' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='嗨嗨'))
    if '晚安' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='晚安，祝你有個好夢=)'))
    if '天氣資訊' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=')'))


    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='輸入無效訊息內容或者該類訊息回覆尚未解鎖😯'))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
