import os
import requests
import datetime

# Needs to be defined
telegram_token = os.getenv('TELEGRAM_TOKEN')
telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
telegram_thread_id = os.getenv('TELEGRAM_THREAD_ID')

now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
message = f'<b>{now}:</b>\nNew strings added!\n\nFind out how to translate Inware at:\nhttps://github.com/evowizz/inware-translations'

data = {
    'chat_id': telegram_chat_id,
    'parse_mode': 'HTML',
    'text': message,
    'disable_web_page_preview': 'true',
    'disable_notification': 'true'
}
if telegram_thread_id:
    data['message_thread_id'] = telegram_thread_id
r = requests.post(f'https://api.telegram.org/bot{telegram_token}/sendMessage', data)
print(r.text)
r.raise_for_status()