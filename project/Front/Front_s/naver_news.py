import requests
from bs4 import BeautifulSoup
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler

url = 'https://search.naver.com/search.naver?query=%EC%98%A8%EC%8B%A4%EA%B0%80%EC%8A%A4&where=news&ie=utf8&sm=nws_hty'
req = requests.get(url)

def get_now():
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.select('div.news_wrap.api_ani_send > div > a')
    press = soup.select('a.info.press')

    title_fin = list()
    press_fin = list()
    url_fin = list()
    for data in title:
        news1 = data.get_text().strip()
        title_fin.append(news1)

    for data2 in press:
        news2 = data2.get_text().strip()
        press_fin.append(news2)

    for link in title:
        url_fin.append(link['href'])

    table = pd.DataFrame({'title':title_fin, 'press':press_fin, 'url':url_fin})
    # table.to_csv('news.csv', encoding='utf-8-sig')
    print(table)

# 5분마다 업데이트
sched = BlockingScheduler()
sched.add_job(get_now, 'interval', minutes=5)
sched.start()