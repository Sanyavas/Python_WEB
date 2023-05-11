import json

import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com/"


def save_to_json(authors, quotes):
    with open('json_fs/authors.json', 'w', encoding='utf-8') as fd:
        json.dump(authors, fd, ensure_ascii=False)
    with open('json_fs/quotes.json', 'w', encoding='utf-8') as fd:
        json.dump(quotes, fd, ensure_ascii=False)

# пагінація по сторінках
def get_urls():
    next_urls = base_url
    flag = True
    urls = [base_url]

    while flag:
        response = requests.get(next_urls)
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.find('ul', class_='pager').find('li', class_='next')
        if content:
            next_page = content.find('a')['href']
            url = base_url + next_page
            urls.append(url)
            next_urls = url
        else:
            flag = False
    return urls


def spider(urls):
    all_quotes = []
    all_authors = []
    list_name_authors = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        content = soup.select('div[class=col-md-8] div[class=quote]')

        for el in content:
            result_quote = {}
            result_author = {}

            # шукаємо та записуємо у словник цитати
            quotes = el.find('span', class_='text').text.strip()
            authors = el.find('small', class_='author').text.strip()
            tags_a = el.find_all('a', class_='tag')
            tags = [tag.text for tag in tags_a]
            result_quote.update({"tags": tags,
                                 "author": authors,
                                 "quote": quotes})
            all_quotes.append(result_quote)

            # перевірка, щоб автор не повторювався
            if authors not in list_name_authors:
                list_name_authors.append(authors)

                # шукаємо та записуємо у словник авторів
                aut_url = base_url + el.find('a')['href']
                aut_urls = requests.get(aut_url)
                soup_au = BeautifulSoup(aut_urls.text, 'lxml')
                fullname = soup_au.find('h3', class_='author-title').text.strip()
                born_date = soup_au.find('span', class_='author-born-date').text.strip()
                born_location = soup_au.find('span', class_='author-born-location').text.strip()
                description = soup_au.find('div', class_='author-description').text.strip()
                result_author.update({"fullname": fullname,
                                      "born_date": born_date,
                                      "born_location": born_location,
                                      "description": description})
                all_authors.append(result_author)

    save_to_json(all_authors, all_quotes)


if __name__ == '__main__':
    spider(get_urls())
    print("End")
