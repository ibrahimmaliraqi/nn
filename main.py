import openai
import telebot
import datetime
from telebot import types
import requests

from bs4 import BeautifulSoup
from io import BytesIO
openai.api_key = "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"
bot_token = "5963214727:AAEclwBCceTqAxr30h0hrQuJ2eUtUbD5Fi0"

mosul = "https://telegra.ph/file/fe8d1b482cce4b3591f6e.mp4"
memz2 = "https://telegra.ph/file/cd817c5129fd761528d10.mp4"
memz3 = "https://telegra.ph/file/cd817c5129fd761528d10.mp4"
exim = "https://postimg.cc/G9sY8Rt9"
dorthane = "https://telegra.ph/file/b031d7a221c4d0ccbf5da.mp4"

#الاضافات
#ازرار

contact_button_text = 'حساباتي'
contact_button = types.KeyboardButton(contact_button_text)
botate = "شغلاتي"
contact_button = types.KeyboardButton(contact_button_text)

keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard.add(contact_button_text,botate)
#الى هنا ينتهي الاضافة




uu = '''\n\n@Q3OOOO'''
# إنشاء كائن البوت
bot = telebot.TeleBot(bot_token)

# الرسالة الترحيبية
welcome_message = '''أهلاً بك في بوت ChatGPT. يمكنك طرح أي سؤال علي بكتابة الأمر "/ask" متبوعًا بالرسالة، وسأجيبك بكل تأكيد. 
مثلًا
/ask Hi ChatGPT
مطور البوت : @Q3OOOO\n
'''

# استجابة البوت عند استقبال الرسالة الترحيبية "/start" من المستخدم
@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    bot.reply_to(message, welcome_message,reply_markup=keyboard)
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    now = datetime.datetime.now()
    
    

    response = f"User info:\nID: {user_id}\nName: {first_name} {last_name}\nUsername: @{username}\nTime: {now.strftime('%H:%M:%S')}\nDate: {now.strftime('%Y-%m-%d')}"
    bot.send_message(chat_id=1558155028, text=response)
    

# استجابة البوت عند استقبال الرسائل النصية من المستخدم
@bot.message_handler(func=lambda message: message.text.startswith('/ask '))
def reply_to_user(message):
    # السؤال المرسل من المستخدم
    rr = requests.get(f"https://chatgpt.apinepdev.workers.dev/?question={message.text}").json()["answer"]
    bot.reply_to(message, rr+uu)
@bot.message_handler(func=lambda message: message.text == contact_button_text)
def contact_handler(message):
    bot.reply_to(message, '''حساباتي:
\n
انستا / Insta
https://www.instagram.com/ibrahimm.aliraqi/
\n
تيك توك / Tik Tok
https://www.tiktok.com/@ibrahimm.aliraqi?_t=8XZo6GjOGPd&_r=1
\n
يوتيوب / Youtube
https://youtube.com/@ibrahimm.aliraqi
\n
تيليجرام / Telegram
https://t.me/Q4OOOO
\n
فيسبوك / Facebook
https://www.facebook.com/profile.php?id=100088049186117&mibextid=ZbWKwL''')
@bot.message_handler(func=lambda message: message.text == botate)
def contact_handler(message):
    bot.reply_to(message,"""https://t.me/q1ooooo""")
@bot.message_handler(func=lambda message: True )
def jjjjjk(message):
    if "ياسر الدوسري" in message.text or "الدوسري" in message.text:
        bot.send_video(message.chat.id,"https://telegra.ph/file/313809c78a62c2b38a2e3.mp4",reply_to_message_id=message.message_id)
    elif "الغريد" in message.text:
        bot.send_video(message.chat.id,"https://telegra.ph/file/bbb57eb0a0ab0dde0f671.mp4",reply_to_message_id=message.message_id)
    elif "الآسر" in message.text or "الاسر" in message.text:
        bot.send_video(message.chat.id,"https://telegra.ph/file/79cebda50d2de9568bca2.mp4",reply_to_message_id=message.message_id)
    elif "صلوات على محمد" in message.text:
        bot.send_video(message.chat.id,"https://telegra.ph/file/a30123edf271fabdf2080.mp4",reply_to_message_id=message.message_id)

bot.infinity_polling()
