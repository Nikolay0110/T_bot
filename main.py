import requests
from pprint import pprint
from datetime import datetime
import telebot
from auth_data import token

def get_data():
    url = 'https://yobit.net/api/3/ticker/btc_usd'
    req = requests.get(url)
    response = req.json()
    # pprint(response)
    sel_price = response['btc_usd']['sell']
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC: {sel_price}")

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет мой друг! Я покажу тебе текущую цену на BTC")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                url = 'https://yobit.net/api/3/ticker/btc_usd'
                req = requests.get(url)
                response = req.json()
                sel_price = response['btc_usd']['sell']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC: {sel_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Что то пошло не так...'
                )
        else:
            bot.send_message(
                message.chat.id,
                'Введена неверная команда...'
            )

    bot.polling()



if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
