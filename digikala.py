import requests
from bs4 import BeautifulSoup
import time 
import schedule
from colorama import Fore


TELEGRAM_TOKEN = '6972371515:AAFNr38MY6ihw2rQDd36Uw6_gIZhCg-qNVw'


def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id' : 5733435053,
        'text' : message
    }
    try :
        response = requests.post(url,data=data)
        print(Fore.BLUE + 'message send')
    except :
        print(Fore.RED + 'message not send')


def price():
    url = 'https://api.digikala.com/v2/product/15596469/'
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36' }
    response = requests.get(url,headers=headers)

    pr = response.json()
    pri = pr['data']['intrack']['eventData']['unitPrice']

    if int(pri) <= 55000000:
        send_message(pri)
    else :
        send_message('قیمت هنوز به مقداری که ثبت شده نزدیک نشده')

price()
schedule.every(1).minute.do(price)

while True :
    schedule.run_pending()
    time.sleep(1)