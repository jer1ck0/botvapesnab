import requests

URL = 'https://vapesnab.ru/prices/download/'

def get_price():
    price = open('price.xlsx', 'wb')
    temp_req = requests.get(URL)
    price.write(temp_req.content) #записываем содержимое в файл; как видите - content запроса
    price.close()