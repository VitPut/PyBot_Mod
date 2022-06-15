import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
from telebot import types

today = date.today()

rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)

menu = types.ReplyKeyboardMarkup( resize_keyboard=True)

btnUSD=types.KeyboardButton(text="🇺🇸 Доллар США")
btnEUR=types.KeyboardButton(text="🇪🇺 Евро")
btnBYN=types.KeyboardButton(text="🇧🇾 Белоруссский рубль")
btnPLN=types.KeyboardButton(text="🇵🇱 Польский злотый")
menu.add(btnUSD, btnEUR)
menu.add(btnBYN, btnPLN)
@bot.message_handler(commands=["start"])
def start(message):
	
	bot.send_message(message.chat.id, "Вбери валюту:", reply_markup=menu)

@bot.message_handler(func = lambda message: message.text=='🇺🇸 Доллар США')
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='🇪🇺 Евро')
def eur(message):
	text = "1 ЕВРО ="+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='🇧🇾 Белоруссский рубль')
def eur(message):
	text = "1 Белоруссский рубль ="+str(rates['BYN'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='🇵🇱 Польский злотый')
def eur(message):
	text = "1 Польский злотый ="+str(rates['PLN'].rate)+"руб."
	bot.send_message(message.chat.id, text)
if __name__=='__main__':
	bot.infinity_polling()