import requests

PAGE_ACCESS_TOKEN = 'EAAOBm7QtZC7cBO4vnYhLgXtIaKxPo6ie43aCDjQt7JkdXvQ3WGgfXg03EfhjKwCi0eVLSBQj6WZAPNqEEfOPgVtHN74hklVlxvX1vKcFiOcEp28uaQQedWo5uNQUSkrYfUsbMB8cBRzwrAes1xXrAq8al6UZB9CFy9xxxx1etA11ZBKWoNASfo730gaNsMCv'

def send_message(sender_id, message):
    url = f"https://graph.facebook.com/v11.0/me/messages"
    payload = {
        "recipient": {"id": sender_id},
        "message": {"text": message},
        "access_token": PAGE_ACCESS_TOKEN
    }
    requests.post(url, json=payload)

# Example usage
send_message('RECIPIENT_ID', 'Hello, this is a test message!')
