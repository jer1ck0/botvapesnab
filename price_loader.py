import requests
import yadisk
import datetime
import telebot
import logging

LOG = "/root/user_scripts/price_loader/vapesnab.log"
URL = 'https://vapesnab.ru/prices/download/'
APP_TOKEN = "AgAEA7qiF5J1AAZeub_cpamIZUn5gyeCcC4cCDs"
TGTOKEN = "1424339301:AAHY4L6MWxe7Mjovg9311Uf3-tCmOUjbud0"
CONTROLLER = "@jer1ck0"
logging.basicConfig(filename = LOG, filemode = 'a', level = logging.DEBUG, format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')

def get_price():
    price = open('/root/user_scripts/price_loader/price.xlsx', 'wb')
    logging.info("request done")
    temp_req = requests.get(URL)
    price.write(temp_req.content)
    logging.info("price was saved")

def notificate():
    tb = telegram.Bot(token=TGTOKEN)
    tb.send_message(CONTROLLER, "123123")
    logging.info("notification sent")

if __name__ == "__main__":
    try:
        get_price()
        date = datetime.datetime.today().strftime("%d-%m-%Y")
        name = "прайс" + date + ".xlsx"
        yd = yadisk.YaDisk(token=APP_TOKEN)
        for all in yd.listdir("/ПРАЙС"):
            ready_to_del = all["name"]
            yd.remove("/ПРАЙС/{}".format(ready_to_del))
        yd.upload("/root/user_scripts/price_loader/price.xlsx", "/ПРАЙС/{}".format(name))
        yd.get_download_link("/ПРАЙС")
        logging.info("All is good")
    except Exception as exname:
        notificate()
        logging.info("Bad fuck")
