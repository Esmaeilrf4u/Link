import requests
import time
from telegram import Bot


BOT_TOKEN = '7505092213:AAGV6Zblq0ykc5Jn6xLhdtmE_KpSYuvFbtc'
CHAT_ID = 105447076
URL = 'https://service2.diplo.de/rktermin/extern/appointment_showMonth.do?locationCode=tehe&realmId=22&categoryId=3069' 

bot = Bot(token=BOT_TOKEN)
was_up = False  # وضعیت قبلی سایت

while True:
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            if not was_up:
                bot.send_message(chat_id=CHAT_ID, text=f'✅ سایت بالا آمد: {URL}')
                was_up = True
            else:
                print('سایت هنوز در دسترسه.')
        else:
            print(f'خطای وضعیت: {response.status_code}')
            was_up = False
    except Exception as e:
        print(f'خطا: {e}')
        was_up = False
    time.sleep(60)
