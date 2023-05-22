import json
import re
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"

current_dir = os.path.dirname(os.path.abspath(__file__))
enemy_loses_json = os.path.join(current_dir, 'json', 'enemy_losses.json')


def get_urls():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4[class=normal] a')
    urls = ['/']
    prefix = '/month.php?month='
    for a in content:
        url = prefix + re.search(r'\d{4}-\d{2}', content[0]['href']).group()  # if all change on 'a'
        urls.append(url)
    return urls


def spider(urls):
    data = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('ul[class=see-also] li[class=gold]', limit=1)
        for el in content:
            result = {}
            date = el.find('span', attrs={"class": "black"}).text

            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()

            except ValueError as err:
                print(f'Error for date: {date} {err}')
                continue
            result.update({'date': date})
            losses = el.find('div').find('div').find('ul')
            for l in losses:
                name, quantity, *_ = l.text.split('—')
                name = name.strip()
                quantity = int(re.search(r'\d+', quantity).group())
                result.update({name: quantity})
            data.append(result)

    return data[0]


def main_enemy():
    url_for_scraping = get_urls()
    r = spider(url_for_scraping)
    r['date'] = r['date'][:10]
    print("---------------------------")
    print(f"Enemy Loses updated for {datetime.today().date()}")
    print("---------------------------")
    print(enemy_loses_json)
    with open('./enemy_losses.json', 'w', encoding='utf-8') as fd:
        json.dump(r, fd, ensure_ascii=False)

    return r


if __name__ == '__main__':
    main_enemy()
