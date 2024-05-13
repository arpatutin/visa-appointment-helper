import telebot
import os

bot = telebot.TeleBot(os.environ["tg_token"])

bot.send_message(-1002122327420, "ПОЙМАНА ЗАПИСЬ В НЕМЕЦКОМ КОНСУЛЬСТВЕ\n@aampelas @rpatutin @younona17")

