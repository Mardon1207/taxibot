from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,CallbackContext,Filters,MessageHandler,CallbackQueryHandler
import json
import os
# TOKEN=os.environ.get("TOKEN")
TOKEN="5850794189:AAFnFdgE9wJ70__uodPKrR6yaIcv_anIu60"
from db import DB
db=DB("data.json")
updater=Updater(TOKEN)
dp=updater.dispatcher

def start(update:Update,context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    taxi=InlineKeyboardButton(text="🚖 Taxi",callback_data="taksi")
    yulovchi=InlineKeyboardButton(text="👤 Yulovchi",callback_data="yulovchi")
    bot_haqida=InlineKeyboardButton(text="📑 Bot haqida",callback_data="bothaqida")
    keyboard=InlineKeyboardMarkup([[
        taxi,yulovchi],[bot_haqida]
    ],resize_keyboard=True)
    text="Assalomu alaykum botimizga xush kelibsiz! \nIltimos o'zingizga kerakli bo'limni tanlang."
    bot.sendMessage(chat_id=chat_id, text=text,reply_markup=keyboard)

def taxi(update:Update,context:CallbackContext):
    query=update.callback_query
    text="Siz Taxi bo'limidasiz. Bu yerda siz yangi e'lon qo'shishingiz, e'loningizni taxrirlashingiz va e'loningizni o'chirishingiz mumkun."
    elonq=InlineKeyboardButton(text="E'lon qo'shish",callback_data="elonqoshish")
    elont=InlineKeyboardButton(text="E'lonni tahrirlash",callback_data="elontahrir")
    elono=InlineKeyboardButton(text="E'lonni o'chirish",callback_data="elonochirish")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[elonq,elont],[elono,ortga]
    ],resize_keyboard=True)
    query.edit_message_text(text=text,reply_markup=keyboard)

def elonqosh(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    try:
        text="Iltimos ismingiz va familyangizni to'liq yozing!"
        query.edit_message_text(text=text)
    except:
        text="Sizni e'loningiz mavjud!"
        query.answer("Sizni e'loningiz mavjud!")

def addism(update:Update,context:CallbackContext):
    query=update.callback_query
    bot=context.bot
    chat_id=update.message.chat.id
    ism=update.message.text
    olsa=InlineKeyboardButton(text="Oltinsoydan Samarqandga",callback_data=f"oltinsam,{chat_id},{ism}")
    olnu=InlineKeyboardButton(text="Oltinsoydan Nurobodga",callback_data=f"oltinnur,{chat_id},{ism}")
    olju=InlineKeyboardButton(text="Oltinsoyan Jumaga",callback_data=f"oltinjum,{chat_id},{ism}")
    olto=InlineKeyboardButton(text="Oltinsoyan Toshkentga",callback_data=f"oltintosh,{chat_id},{ism}")
    nusa=InlineKeyboardButton(text="Nuroboddan Samarqandga",callback_data=f"nursam,{chat_id},{ism}")
    nuju=InlineKeyboardButton(text="Nuroboddan Jumaga",callback_data=f"nurjum,{chat_id},{ism}")
    nuto=InlineKeyboardButton(text="Nuroboddan Toshkentga",callback_data=f"nurtosh,{chat_id},{ism}")
    boshqa=InlineKeyboardButton(text="Boshqa",callback_data="boshqa1")
    keyboard=InlineKeyboardMarkup([[olnu],[olsa],[olju],[olto],[nusa],[nuju],[nuto],[boshqa]],resize_keyboard=True)
    text="Qanday yunalishda qatnaysiz"
    bot.sendMessage(text=text,chat_id=chat_id,reply_markup=keyboard)

def qoshish(update:Update,context:CallbackContext):
    query=update.callback_query
    data=query.data
    chat_id=data.split(",")[1]
    ism=data.split(',')[2]
    qayer=data.split(',')[0]
    db.save(chat_id=chat_id,ism=ism,qayer=qayer)
    text="Ma'lumotlar saqlani"
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[ortga]
    ],resize_keyboard=True)
    query.edit_message_text(text=text,reply_markup=keyboard)

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CallbackQueryHandler(taxi,pattern="taksi"))
dp.add_handler(CallbackQueryHandler(elonqosh,pattern="elonqoshish"))
dp.add_handler(MessageHandler(Filters.text,addism))
dp.add_handler(CallbackQueryHandler(qoshish,pattern="oltinsam"))
updater.start_polling()
updater.idle()