import os
from dotenv import load_dotenv
import telebot

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not found. Check your .env file.")

bot = telebot.TeleBot(BOT_TOKEN)

class Country:
    def __init__(self, capital, population, currency, region):
        self.capital = capital
        self.population = population
        self.currency = currency
        self.region = region

    def __str__(self):
        return (f"🏛 Capital: {self.capital}\n"
                f"👥 Population: {self.population}\n"
                f"🪙 Currency: {self.currency}\n"
                f"📍 Region: {self.region}")

DATA = {
    "cambodia": Country("Phnom Penh", "16.9 million", "Riel (KHR)", "Southeast Asia"),
    "japan": Country("Tokyo", "125.1 million", "Yen (JPY)", "East Asia"),
    "france": Country("Paris", "67.7 million", "Euro (EUR)", "Western Europe"),
}

@bot.message_handler(func=lambda message: True)
def reply_capital(message):
    country = message.text.strip().lower()
    info = DATA.get(country)

    if info:
        bot.reply_to(message, str(info))
    else:
        bot.reply_to(message, f"❌ '{message.text}' doesn't look like a valid country name. Try again!")

print("Bot starting...")
bot.infinity_polling()