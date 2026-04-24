import telebot
from telebot import types
from flask import Flask
from threading import Thread

# МИНИ-СЕРВЕР ДЛЯ RENDER
app = Flask('')
@app.route('/')
def home(): return "I'm alive"
def run(): app.run(host='0.0.0.0', port=8080)

# ТВОЙ ТОКЕН (ПРОВЕРЬ ЕГО!)
TOKEN = '8643102833:AAFT3-4fcuu5l5OOEeGloVBx83loSIKrVb0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📱 Смартфони", "💻 Ноутбуки")
    bot.send_message(message.chat.id, "🛒 Демо-магазин працює!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "📱 Смартфони":
        bot.send_message(message.chat.id, "📱 Тут будуть iPhone")
    elif message.text == "💻 Ноутбуки":
        bot.send_message(message.chat.id, "💻 Тут будуть MacBook")

if __name__ == "__main__":
    Thread(target=run).start()
    bot.infinity_polling()
    
