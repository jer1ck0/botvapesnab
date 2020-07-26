import requests
import telebot
from telebot import apihelper
import  apiai, json

BOT = '819833514:AAGQOJY_l6NvSIX13mU2GTTjx25WecDpzks'
URL = 'https://vapesnab.ru/prices/download/'
TELE_URL = 'https://telegg.ru/orig/bot{0}/{1}'
DF_TOKEN = '8016929c91c544b9a89589e5cca134f2'
DATA = {
    "login": "opt@vapeskladnn.ru",
    "password": "251499"
}
setattr(apihelper,'API_URL',TELE_URL)

def get_price():
    price = open('price.xlsx', 'wb')
    temp_req = requests.get(URL)
    price.write(temp_req.content) #записываем содержимое в файл; как видите - content запроса
    price.close()

bot = telebot.TeleBot(BOT)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.from_user.id, 'Привет, я бот VapeSnab')

@bot.message_handler(commands=['price','прайс'])
def send_price(message):
    with open('price.xlsx', 'rb') as file:
        get_price()
        bot.send_document(message.from_user.id, file)

@bot.message_handler(content_types=['text'])
def dialog_custom(message):
    request = apiai.ApiAI(DF_TOKEN).text_request()
    request.lang = 'ru'
    request.session_id = 'vapesnab'
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(message.from_user.id, response)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял')

bot.polling()  # запускаем бота