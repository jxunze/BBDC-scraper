import os
import parser
import telebot
from itertools import islice

API_TOKEN = os.environ.get("TELEBOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

@bot.message_handler(commands=['test'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user.id}")
    bot.reply_to(message, f"{message.from_user.first_name}")
    bot.reply_to(message, f"{message.from_user.last_name}")
    bot.reply_to(message, f"{message.from_user.username}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, enter /scrape to get the available TPDS dates.")


@bot.message_handler(commands=['scrape'])
def send_available_dates(message):
    bot.send_message(message.chat.id, f"_Sending request to server..._", parse_mode="MARKDOWN")
    dates = parser.obtain_dates()
    bot.send_message(message.chat.id, "Here are the 3 earliest dates:\n")
    truncated_dates = dict(islice(dates.items(), 3))
    for x in truncated_dates:
        bot.send_message(message.chat.id, f"*{x}*\n{truncated_dates[x]}", parse_mode="MARKDOWN")

@bot.message_handler(func=lambda m: True)
def all_other_messages(message):
    bot.send_message(message.chat.id, f"Welcome! I am a BBDC Driving Simulator Scraping bot.\nOnce you set your environment variables accordingly, enter /scrape and I will scrape the earliest dates for you.", parse_mode="MARKDOWN")

if __name__ == "__main__":
    bot.infinity_polling()