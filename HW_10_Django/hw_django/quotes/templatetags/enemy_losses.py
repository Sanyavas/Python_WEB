import json
import os
import re
from datetime import datetime
import requests

from bs4 import BeautifulSoup

# BASE_DIR = Path(__file__).resolve().parent.parent.parent
current_dir = os.path.dirname(os.path.abspath(__file__))
enemy_loses_json = os.path.join(current_dir, 'json', 'enemy_losses.json')
base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"
# json_path = 'hw_django/quotes/json/enemy_losses.json'
# json_path = str(pathlib.PurePath(BASE_DIR, 'hw_django', 'quotes', 'json', 'enemy_losses.json').stem)


def get_urls():
    """
    The function uses the requests library to get the html from the base_url, then parses it using BeautifulSoup.
    """
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4[class=normal] a')
    urls = ['/']
    prefix = '/month.php?month='
    for a in content:
        url = prefix + re.search(r'\d{4}-\d{2}', a['href']).group()  # if all change on 'a'
        urls.append(url)
    # print(urls)
    return urls


def spider(urls):
    """
    The spider function takes a list of urls and returns a list of dictionaries.
    Each dictionary contains the date, name and quantity for each loss.
    """
    data = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('ul[class=see-also] li[class=gold]')
        for el in content:
            result = {}
            date = el.find('span', attrs={"class": "black"}).text

            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()

            except ValueError as err:
                # print(f'Error for date: {date} {err}')
                continue
            result.update({'date': date})
            losses = el.find('div').find('div').find('ul')
            for loss in losses:
                name, quantity, *_ = loss.text.split('—')
                name = name.strip()
                quantity = int(re.search(r'\d+', quantity).group())
                result.update({name: quantity})
            data.append(result)

    return data


def main_enemy():
    """
    The main_enemy function scrapes the enemy losses page of the website and returns a list of dictionaries.
    """
    url_for_scraping = get_urls()
    r = spider(url_for_scraping)
    r[0]['date'] = r[0]['date'][:10]
    print("----------------------------------------")
    print(f"Enemy Loses updated json for {r[0]['date']}")
    print("----------------------------------------")

    with open(enemy_loses_json, 'w', encoding='utf-8') as fd:
        json.dump(r, fd, ensure_ascii=False, indent=4)

    return r


if __name__ == '__main__':
    main_enemy()

