import telebot
import requests


bot = telebot.TeleBot("", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    msg_text = message.text
    msg_text = msg_text.replace('/start ', '')

    response = requests.get(
        'http://api.giphy.com/v1/gifs/search',
        params={
            'q': msg_text,
            'limit': 10,
            'api_key': 'GmsbaH8MUOADH1bkRG7LFfgBseo0dQma'
        }
    )

    data = response.json()
    for obj in data['data']:
        url = obj['images']['original']['url']
        bot.send_animation(message.from_user.id, url)


bot.infinity_polling()
