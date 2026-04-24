import telebot
from telebot import types
from flask import Flask
from threading import Thread
import time

# --- МИНИ-СЕРВЕР ДЛЯ RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Shop is Alive"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()
# -------------------------

# Твой полный токен из BotFather
TOKEN = '8643102833:AAFT3-4fcuu5l5OOEeGloVBx83loSIKrVb0'
bot = telebot.TeleBot(TOKEN)

# Данные о товарах для примера
products = {
    "iphone": {"name": "iPhone 15 Pro", "price": "45 000 грн", "img": "https://pixabay.com"},
    "macbook": {"name": "MacBook Air M2", "price": "52 000 грн", "img": "https://pixabay.com"}
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📱 Смартфони", "💻 Ноутбуки", "📞 Підтримка")
    bot.send_message(message.chat.id, "🛒 Вітаємо у Demo-магазині!\nОберіть категорію товарів:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "📱 Смартфони":
        p = products["iphone"]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(f"Купити за {p['price']}", callback_data="buy"))
        bot.send_photo(message.chat.id, p["img"], caption=f"🔥 **{p['name']}**\nНайкраща ціна сьогодні!", reply_markup=markup, parse_mode="Markdown")

    elif message.text == "💻 Ноутбуки":
        p = products["macbook"]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(f"Купити за {p['price']}", callback_data="buy"))
        bot.send_photo(message.chat.id, p["img"], caption=f"🚀 **{p['name']}**\nПотужність та стиль.", reply_markup=markup, parse_mode="Markdown")
    
    elif message.text == "📞 Підтримка":
        bot.send_message(message.chat.id, "Напишіть нашому менеджеру: @MuichiroHGP")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "buy":
        bot.answer_callback_query(call.id, "Замовлення прийнято!")
        bot.send_message(call.message.chat.id, "✅ **Дякуємо!**\nЦе демонстраційний бот. У реальному боті тут би прийшла заявка власнику магазину.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
    
