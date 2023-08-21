from flask import Flask, request
from telegram.ext import Dispatcher
from telegram import Bot, Update

from telegram.ext import (
    Updater, 
    MessageHandler, 
    CommandHandler, 
    CallbackQueryHandler, 
    Filters, 
    )

from handlers import (
    start,
    taxi,
    ortga2,
    elonqosh,
    korish,
    qaytish,
    elonoch,
    addism,
    rasm,
    qoshish,
    yulovchi,
    elonkor,
    back,
    next,
    chiqarish,
    tanlash,
    ortgayul,
    oldin,
    keyin,
    ortgayul1,
    boshqa,
    haqida,
    ortgaqayt
    )
from settings import TOKEN

app = Flask(__name__)

@app.route("/setwebhook/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
    
        bot = Bot(TOKEN)
        dp = Dispatcher(bot, None, workers=0)
        data = request.get_json()

        update = Update.de_json(data, bot)

        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CallbackQueryHandler(taxi,pattern="taksi"))
        dp.add_handler(CallbackQueryHandler(ortga2,pattern="ortga2"))
        dp.add_handler(CallbackQueryHandler(elonqosh,pattern="elonqoshish"))
        dp.add_handler(CallbackQueryHandler(korish,pattern="korish"))
        dp.add_handler(CallbackQueryHandler(qaytish,pattern="qaytish"))
        dp.add_handler(CallbackQueryHandler(elonoch,pattern="elonochirish"))
        dp.add_handler(MessageHandler(Filters.photo,addism))
        dp.add_handler(MessageHandler(Filters.contact,rasm))
        dp.add_handler(CallbackQueryHandler(qoshish,pattern="qush,"))
        dp.add_handler(CallbackQueryHandler(yulovchi,pattern="yulovchi"))
        dp.add_handler(CallbackQueryHandler(elonkor,pattern="elonkorish"))
        dp.add_handler(CallbackQueryHandler(back,pattern="back"))
        dp.add_handler(CallbackQueryHandler(next,pattern="nextn"))
        dp.add_handler(CallbackQueryHandler(chiqarish,pattern="qwe,"))
        dp.add_handler(CallbackQueryHandler(oldin,pattern="oldin"))
        dp.add_handler(CallbackQueryHandler(keyin,pattern="keyin"))
        dp.add_handler(CallbackQueryHandler(tanlash,pattern="tanlash"))
        dp.add_handler(CallbackQueryHandler(ortgayul,pattern="ortgayul"))
        dp.add_handler(CallbackQueryHandler(ortgayul1,pattern="ortgayol"))
        dp.add_handler(CallbackQueryHandler(boshqa,pattern="boshqa1"))
        dp.add_handler(CallbackQueryHandler(haqida,pattern="bothaqida"))
        dp.add_handler(CallbackQueryHandler(ortgaqayt,pattern="ortgaqayt"))
        print("OK")
        return "ok"
    
    else:
        return "Not allowed GET request"