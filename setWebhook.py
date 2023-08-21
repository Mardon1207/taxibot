import telegram

import os 
from settings import TOKEN
url = "https://mardon.pythonanywhere.com/taxi/"


bot = telegram.Bot(TOKEN)


# bot.delete_webhook()
bot.set_webhook(url)
print(bot.get_webhook_info())