import yadisk
import datetime
import loader

APP_TOKEN = "AgAEA7qiF5J1AAZeub_cpamIZUn5gyeCcC4cCDs"

loader.get_price()
date = datetime.datetime.today().strftime("%d-%m-%Y")
name = "прайс" + date + ".xlsx"
yd = yadisk.YaDisk(token=APP_TOKEN)
for all in yd.listdir("/ПРАЙС"):
    ready_to_del = all["name"]
    yd.remove("/ПРАЙС/{}".format(ready_to_del))
yd.upload("price.xlsx", "/ПРАЙС/{}".format(name))
yd.get_download_link("/ПРАЙС")
print(yd.get_code_url())
