import os
import requests
from flask import Flask, request

app = Flask(__name__)

PAGE_ACCESS_TOKEN = os.environ.get('EAAOBm7QtZC7cBO4vnYhLgXtIaKxPo6ie43aCDjQt7JkdXvQ3WGgfXg03EfhjKwCi0eVLSBQj6WZAPNqEEfOPgVtHN74hklVlxvX1vKcFiOcEp28uaQQedWo5uNQUSkrYfUsbMB8cBRzwrAes1xXrAq8al6UZB9CFy9xxxx1etA11ZBKWoNASfo730gaNsMCv')
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Verification token mismatch', 403
    elif request.method == 'POST':
        data = request.json
        if data['object'] == 'page':
            for entry in data['entry']:
                for event in entry['messaging']:
                    handle_event(event)
        return 'EVENT_RECEIVED', 200

def handle_event(event):
    if 'message' in event:
        sender_id = event['sender']['id']
        message = event['message']['text']
        send_message(sender_id, "We received your message: " + message)
    elif 'comment_id' in event:
        comment_id = event['comment_id']
        reply_comment(comment_id, "We contacted you")
        send_message(event['from']['id'], "Your direct message text here")

def reply_comment(comment_id, message):
    url = f"https://graph.facebook.com/v11.0/{comment_id}/comments"
    payload = {
        "message": message,
        "access_token": PAGE_ACCESS_TOKEN
    }
    requests.post(url, data=payload)

def send_message(sender_id, message):
    url = f"https://graph.facebook.com/v11.0/me/messages"
    payload = {
        "recipient": {"id": sender_id},
        "message": {"text": message},
        "access_token": PAGE_ACCESS_TOKEN
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=True)
