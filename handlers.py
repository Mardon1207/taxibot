from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    InputMediaPhoto
    )
from telegram.ext import (
    CallbackContext
    )
from db import DB
db = DB("/home/Mardon/taxibot/data.json")
from rasm import DB
rasmdb =DB("/home/Mardon/taxibot/rasm.json")
from contact import DB
contactdb =DB("/home/Mardon/taxibot/rasm.json")

def start(update:Update,context:CallbackContext):
    chat_id=update.message.chat.id
    print(chat_id)
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
    elono=InlineKeyboardButton(text="E'lonni o'chirish",callback_data="elonochirish")
    korish=InlineKeyboardButton(text="E'loni ko'rish",callback_data="korish")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[elonq,elono],[korish,ortga]
    ],resize_keyboard=True)
    query.edit_message_text(text=text,reply_markup=keyboard)

def elonqosh(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    bot=context.bot
    if len(db.izla(chat_id=chat_id))==0:
        query=update.callback_query
        button = KeyboardButton("Telefon raqamni yuborish", request_contact=True)
        keyboard = ReplyKeyboardMarkup([[button]],one_time_keyboard=True, resize_keyboard=True)
        query.delete_message()
        bot.send_message(chat_id, "Iltimos, telefon raqamingizni yuboring:", reply_markup=keyboard)
    else:
        query.answer("Sizni e'loningiz mavjud!")

def korish(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    try:
        data=db.izla(chat_id)
        chat_id=query.message.chat.id
        bot = context.bot
        ism=data[0]['ism']
        phone=data[0]['phone']
        qayer=data[0]["qayer"]
        rasm=data[0]['rasm']
        ortga=InlineKeyboardButton(text="Ortga",callback_data="qaytish")
        keyboard=InlineKeyboardMarkup([[ortga]
        ],resize_keyboard=True)
        text=f'Ismi {ism}\nTelfon raqami:  {phone}\nManzili:  {qayer[0]} {qayer[1]}'
        query.delete_message()
        bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
    except:
        query.answer("Sizni e'loningiz mavjud emas!!!")
    
def qaytish(update:Update,context:CallbackContext):
    query=update.callback_query
    bot=context.bot
    chat_id=query.message.chat.id
    text="Siz Taxi bo'limidasiz. Bu yerda siz yangi e'lon qo'shishingiz, e'loningizni taxrirlashingiz va e'loningizni o'chirishingiz mumkun."
    elonq=InlineKeyboardButton(text="E'lon qo'shish",callback_data="elonqoshish")
    elono=InlineKeyboardButton(text="E'lonni o'chirish",callback_data="elonochirish")
    korish=InlineKeyboardButton(text="E'loni ko'rish",callback_data="korish")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[elonq,elono],[korish,ortga]
    ],resize_keyboard=True)
    query.delete_message()
    bot.send_message(chat_id,text=text,reply_markup=keyboard)

def rasm(update:Update,context:CallbackContext):
    bot=context.bot
    query=update.callback_query
    chat_id=update.message.chat.id
    contact=update.message.contact.phone_number
    contactdb.save(contact=contact,chat_id=chat_id)
    text="Avtomobilingizning rasmini yuboring"
    bot.send_message(chat_id=chat_id,text=text)

def addism(update:Update,context:CallbackContext):
    # query=update.callback_query
    bot=context.bot
    rasm=update.message.photo[-1]['file_id']
    chat_id=update.message.chat.id
    rasmdb.save(chat_id,rasm)
    ism=update.message.chat.username
    olsa=InlineKeyboardButton(text="Oltinsoydan Samarqandga",callback_data=f"qush,Oltinsoydan,Samarqanga")
    olnu=InlineKeyboardButton(text="Oltinsoydan Nurobodga",callback_data=f"qush,Oltinsoydan,Nurobodga")
    olju=InlineKeyboardButton(text="Oltinsoyan Jumaga",callback_data=f"qush,Oltinsoyan,Jumaga")
    olto=InlineKeyboardButton(text="Oltinsoyan Toshkentga",callback_data=f"qush,Oltinsoyan,Toshkentga")
    nusa=InlineKeyboardButton(text="Nuroboddan Samarqandga",callback_data=f"qush,Nuroboddan,Samarqandga")
    nuju=InlineKeyboardButton(text="Nuroboddan Jumaga",callback_data=f"qush,Nuroboddan,Jumaga")
    nuto=InlineKeyboardButton(text="Nuroboddan Toshkentga",callback_data=f"qush,Nuroboddan,Toshkentga")
    boshqa=InlineKeyboardButton(text="Boshqa",callback_data="boshqa1")
    keyboard=InlineKeyboardMarkup([[olnu],[olsa],[olju],[olto],[nusa],[nuju],[nuto],[boshqa]],resize_keyboard=True)
    text="Qanday yunalishda qatnaysiz"
    bot.send_message(str(chat_id),text,reply_markup=keyboard)

def qoshish(update:Update,context:CallbackContext):
    query=update.callback_query
    data=query.data
    user=query.message.chat.username
    havola=f"https://t.me/{user}"
    ism=query.message.chat.username
    chat_id=query.message.chat.id
    qayer=data.split(',')[1:]
    phone=contactdb.izla(chat_id)[0]['contact']
    rasm=rasmdb.izla(chat_id)[0]['rasm']
    db.save(chat_id=chat_id,ism=ism,phone=phone,havola=havola,qayer=qayer,rasm=rasm)
    rasmdb.remove(chat_id)
    contactdb.remove(chat_id)
    query.answer("Ma'lumotlar saqlandi")
    text="Siz Taxi bo'limidasiz. Bu yerda siz yangi e'lon qo'shishingiz, e'loningizni taxrirlashingiz va e'loningizni o'chirishingiz mumkun."
    elonq=InlineKeyboardButton(text="E'lon qo'shish",callback_data="elonqoshish")
    elono=InlineKeyboardButton(text="E'lonni o'chirish",callback_data="elonochirish")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[elonq,elono],[ortga]
    ],resize_keyboard=True)
    query.edit_message_text(text=text,reply_markup=keyboard)

def elonoch(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    if len(db.izla(chat_id=chat_id))!=0:
        db.remove(chat_id)
        query.answer("E'loningiz o'chirildi!")
    else:
        query.answer("E'lon mavjud emas!!!")

def ortga2(update:Update,context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    taxi=InlineKeyboardButton(text="🚖 Taxi",callback_data="taksi")
    yulovchi=InlineKeyboardButton(text="👤 Yulovchi",callback_data="yulovchi")
    bot_haqida=InlineKeyboardButton(text="📑 Bot haqida",callback_data="bothaqida")
    keyboard=InlineKeyboardMarkup([[
        taxi,yulovchi],[bot_haqida]
    ],resize_keyboard=True)
    text="Assalomu alaykum botimizga xush kelibsiz! \nIltimos o'zingizga kerakli bo'limni tanlang."
    query.edit_message_text(text=text,reply_markup=keyboard)

def yulovchi(update:Update,context:CallbackContext):
    query=update.callback_query
    text="Siz Yulovchi bo'limidasiz. Bu yerda siz yangi e'lon qo'shishingiz, e'loningizni taxrirlashingiz va e'loningizni o'chirishingiz mumkun."
    elonk=InlineKeyboardButton(text="E'lonlarni ko'rish",callback_data="elonkorish")
    manzil=InlineKeyboardButton(text="Manzilni tanlash",callback_data="tanlash")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[elonk,manzil],[ortga]
    ],resize_keyboard=True)
    query.edit_message_text(text=text,reply_markup=keyboard)

def elonkor(update:Update,context:CallbackContext):
    query=update.callback_query
    m=0
    lst=db.hamma()      
    chat_id=query.message.chat.id
    bot = context.bot
    try:
        ism=lst[m]['ism']
        phone=lst[m]['phone']
        havola=lst[m]['havola']
        qayer=lst[m]["qayer"]
        rasm=lst[m]['rasm']
        k=[]
        back=InlineKeyboardButton(text="⏪",callback_data=f"back,{m}")
        nextn=InlineKeyboardButton(text="⏩",callback_data=f"nextn,{m}")
        max=len(lst)
        if m>0 and m<max-1:
            k.append([back,nextn])
        elif m==max-1 and max!=1:
            k.append([back])
        elif m==0 and max!=1:
            k.append([nextn])
        ortga2=InlineKeyboardButton(text="Ortga",callback_data="ortgayul")
        lichka=InlineKeyboardButton(text="Bog'lansh",url=havola)
        k.append([lichka])
        k.append([ortga2])
        keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
        text=f'Ismi {ism}\nTelfon raqami:  {phone}\nManzili:  {qayer[0]} {qayer[1]}'
        query.delete_message()
        bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
    except:
        query.answer("Bu yunalishga hechkim e'lon bermagan")

def back(update:Update,context:CallbackContext):
    query=update.callback_query
    m=int(query.data.split(",")[1])
    m=m-1
    lst=db.hamma()      
    chat_id=query.message.chat.id
    bot = context.bot
    try:
        ism=lst[m]['ism']
        phone=lst[m]['phone']
        havola=lst[m]['havola']
        qayer=lst[m]["qayer"]
        rasm=lst[m]['rasm']
        k=[]
        back=InlineKeyboardButton(text="⏪",callback_data=f"back,{m}")
        nextn=InlineKeyboardButton(text="⏩",callback_data=f"nextn,{m}")
        max=len(lst)
        if m>0 and m<max-1:
            k.append([back,nextn])
        elif m==max-1:
            k.append([back])
        elif m==0:
            k.append([nextn])
        ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortgayul")
        lichka=InlineKeyboardButton(text="Bog'lansh",url=havola)
        k.append([lichka])
        k.append([ortga2])
        keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
        text=f'Ismi {ism}\nTelfon raqami:  {phone}\nManzili:  {qayer}'
        query.delete_message()
        bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
    except:
        query.answer("Bu yunalishga hechkim e'lon bermagan")

def next(update:Update,context:CallbackContext):
    query=update.callback_query
    m=int(query.data.split(",")[1])
    m=m+1
    lst=db.hamma()      
    chat_id=query.message.chat.id
    bot = context.bot
    try:
        ism=lst[m]['ism']
        phone=lst[m]['phone']
        havola=lst[m]['havola']
        qayer=lst[m]["qayer"]
        rasm=lst[m]['rasm']
        k=[]
        back=InlineKeyboardButton(text="⏪",callback_data=f"back,{m}")
        nextn=InlineKeyboardButton(text="⏩",callback_data=f"nextn,{m}")
        max=len(lst)
        if m>0 and m<max-1:
            k.append([back,nextn])
        elif m==max-1:
            k.append([back])
        elif m==0:
            k.append([nextn])
        ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortgayul")
        lichka=InlineKeyboardButton(text="Bog'lansh",url=havola)
        k.append([lichka])
        k.append([ortga2])
        keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
        text=f'Ismi {ism}\nTelfon raqami:  {phone}\nManzili:  {qayer}'
        query.delete_message()
        bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
    except:
        query.answer("Bu yunalishga hechkim e'lon bermagan")

def tanlash(update:Update,context:CallbackContext):
    query=update.callback_query
    olsa=InlineKeyboardButton(text="Oltinsoydan Samarqandga",callback_data=f"qwe,Oltinsoydan,Samarqanga")
    olnu=InlineKeyboardButton(text="Oltinsoydan Nurobodga",callback_data=f"qwe,Oltinsoydan,Nurobodga")
    olju=InlineKeyboardButton(text="Oltinsoyan Jumaga",callback_data=f"qwe,Oltinsoyan,Jumaga")
    olto=InlineKeyboardButton(text="Oltinsoyan Toshkentga",callback_data=f"qwe,Oltinsoyan,Toshkentga")
    nusa=InlineKeyboardButton(text="Nuroboddan Samarqandga",callback_data=f"qwe,Nuroboddan,Samarqandga")
    nuju=InlineKeyboardButton(text="Nuroboddan Jumaga",callback_data=f"qwe,Nuroboddan,Jumaga")
    nuto=InlineKeyboardButton(text="Nuroboddan Toshkentga",callback_data=f"qwe,Nuroboddan,Toshkentga")
    boshqa=InlineKeyboardButton(text="Boshqa",callback_data="boshqa1")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortgayol")
    keyboard=InlineKeyboardMarkup([[olnu],[olsa],[olju],[olto],[nusa],[nuju],[nuto],[boshqa],[ortga]],resize_keyboard=True)
    text="Qanday yunalishda qatnaysiz"
    query.edit_message_text(text=text,reply_markup=keyboard)

def chiqarish(update:Update,context:CallbackContext):
    query=update.callback_query
    b=[]
    b.append(query.data.split(",")[1])
    b.append(query.data.split(",")[2])
    m=0
    lst=db.manzil(b)      
    chat_id=query.message.chat.id
    bot = context.bot
    try:
        ism=lst[m]['ism']
        phone=lst[m]['phone']
        havola=lst[m]['havola']
        qayer=lst[m]["qayer"]
        rasm=lst[m]['rasm']
        k=[]
        back=InlineKeyboardButton(text="⏪",callback_data=f"oldin,{m}")
        nextn=InlineKeyboardButton(text="⏩",callback_data=f"keyin,{m}")
        max=len(lst)
        if m>0 and m<max-1:
            k.append([back,nextn])
        elif m==max-1 and max!=1:
            k.append([back])
        elif m==0 and max!=1:
            k.append([nextn])
        ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortgaqayt")
        lichka=InlineKeyboardButton(text="Bog'lansh",url=havola)
        k.append([lichka])
        k.append([ortga2])
        keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
        text=f'Ismi {ism}\nTelfon raqami:  {phone}\nManzili:  {qayer[0]} {qayer[1]}'
        query.delete_message()
        bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
    except:
        query.answer("Bu yunalishga hechkim e'lon bermagan")

def oldin(update:Update,context:CallbackContext):
    query=update.callback_query
    b=[]
    b.append(query.data.split(",")[1])
    b.append(query.data.split(",")[2])
    m=int(query.data.split(",")[1])
    m=m-1
    lst=db.manzil(b)        
    chat_id=query.message.chat.id
    bot = context.bot
    try:
        ism=lst[m]['ism']
        phone=lst[m]['phone']
        havola=lst[m]['havola']
        qayer=lst[m]["qayer"]
        rasm=lst[m]['rasm']
        k=[]
        back=InlineKeyboardButton(text="⏪",callback_data=f"oldin,{m}")
        nextn=InlineKeyboardButton(text="⏩",callback_data=f"keyin,{m}")
        max=len(lst)
        if m>0 and m<max-1:
            k.append([back,nextn])
        elif m==max-1 and max!=1:
            k.append([back])
        elif m==0 and max!=1:
            k.append([nextn])
        ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortga2")
        lichka=InlineKeyboardButton(text="Bog'lansh",url=havola)
        k.append([lichka])
        k.append([ortga2])
        keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
        text=f'Ismi {ism}\nTelfon raqami:  {phone}\nManzili:  {qayer}'
        query.delete_message()
        bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
    except:
        query.answer("Bu yunalishga hechkim e'lon bermagan")

def keyin(update:Update,context:CallbackContext):
    query=update.callback_query
    b=[]
    b.append(query.data.split(",")[1])
    b.append(query.data.split(",")[2])
    m=int(query.data.split(",")[1])
    try:
        m=m+1
        lst=db.manzil(b)      
        chat_id=query.message.chat.id
        bot = context.bot
        ism=lst[m]['ism']
        phone=lst[m]['phone']
        havola=lst[m]['havola']
        qayer=lst[m]["qayer"]
        rasm=lst[m]['rasm']
        k=[]
        back=InlineKeyboardButton(text="⏪",callback_data=f"oldin,{m}")
        nextn=InlineKeyboardButton(text="⏩",callback_data=f"keyin,{m}")
        max=len(lst)
        if m>0 and m<max-1:
            k.append([back,nextn])
        elif m==max-1:
            k.append([back])
        elif m==0:
            k.append([nextn])
        ortga2=InlineKeyboardButton(text="Ortga",callback_data=f"ortga2")
        lichka=InlineKeyboardButton(text="Bog'lansh",url=havola)
        k.append([lichka])
        k.append([ortga2])
        keyboard=InlineKeyboardMarkup(k,resize_keyboard=True)
        text=f'Ismi {ism}\nTelfon raqami:  {phone}\nManzili:  {qayer}'
        query.delete_message()
        bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
    except:
        query.answer("Bu yunalishga hechkim e'lon bermagan")

def ortgayul(update:Update,context:CallbackContext):
    query=update.callback_query
    bot=context.bot
    chat_id=query.message.chat.id
    text="Siz Yulovchi bo'limidasiz. Bu yerda siz yangi e'lon qo'shishingiz, e'loningizni taxrirlashingiz va e'loningizni o'chirishingiz mumkun."
    elonk=InlineKeyboardButton(text="E'lonlarni ko'rish",callback_data="elonkorish")
    manzil=InlineKeyboardButton(text="Manzilni tanlash",callback_data="tanlash")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[elonk,manzil],[ortga]
    ],resize_keyboard=True)
    query.delete_message()
    bot.sendMessage(chat_id=chat_id,text=text,reply_markup=keyboard)

def ortgayul1(update:Update,context:CallbackContext):
    query=update.callback_query
    text="Siz Yulovchi bo'limidasiz. Bu yerda siz yangi e'lon qo'shishingiz, e'loningizni taxrirlashingiz va e'loningizni o'chirishingiz mumkun."
    elonk=InlineKeyboardButton(text="E'lonlarni ko'rish",callback_data="elonkorish")
    manzil=InlineKeyboardButton(text="Manzilni tanlash",callback_data="tanlash")
    ortga=InlineKeyboardButton(text="Ortga",callback_data="ortga2")
    keyboard=InlineKeyboardMarkup([[elonk,manzil],[ortga]
    ],resize_keyboard=True)
    query.edit_message_text(text=text,reply_markup=keyboard)

def boshqa(update:Update,context:CallbackContext):
    query=update.callback_query
    query.answer("Boshqa yunalishlar hali kiritilmagan!!!")

def haqida(update:Update,context:CallbackContext):
    query=update.callback_query
    bot=context.bot
    m=0    
    chat_id=query.message.chat.id
    rasm="AgACAgIAAxkBAAIDA2Tfp_ALzRhQQTOa-jq7xrFRP309AAKpzDEb1nUBSyh9wQyBQAdjAQADAgADeAADMAQ"
    ortga=InlineKeyboardButton(text="Ortga",callback_data=f"ortgaqayt")
    lichka=InlineKeyboardButton(text="Bog'lansh",url="https://t.me/S_M_M_1207")
    keyboard=InlineKeyboardMarkup([[lichka],[ortga]],resize_keyboard=True)
    text="Bu bot Mardon Sultonov tomonidan tayorlandi\nAgarda bot bilan biror kamchilik yoki muammo bulsa pastdagi tugma bilan men bilan bog'lanishingiz mumkun\n\nBotimiz sizga manzur bo'ladi degan umiddaman!!!"
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=rasm,caption=text,reply_markup=keyboard)
       
def ortgaqayt(update:Update,context:CallbackContext):
    query=update.callback_query
    bot=context.bot
    chat_id=query.message.chat.id
    taxi=InlineKeyboardButton(text="🚖 Taxi",callback_data="taksi")
    yulovchi=InlineKeyboardButton(text="👤 Yulovchi",callback_data="yulovchi")
    bot_haqida=InlineKeyboardButton(text="📑 Bot haqida",callback_data="bothaqida")
    keyboard=InlineKeyboardMarkup([[
        taxi,yulovchi],[bot_haqida]
    ],resize_keyboard=True)
    text="Assalomu alaykum botimizga xush kelibsiz! \nIltimos o'zingizga kerakli bo'limni tanlang."
    query.delete_message()
    bot.send_message(chat_id=chat_id,text=text,reply_markup=keyboard)