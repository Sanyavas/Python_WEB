import json

from odm_mongoengine.models import Author, TextQuote, Quote


def load_json(file_author, file_quote):
    with open(file_author, 'r', encoding='utf-8') as f:
        authors = json.load(f)
        for ar in authors:
            author = Author(
                name=ar['fullname'],
                born_date=ar['born_date'],
                born_location=ar['born_location'],
                description=ar['description']
            ).save()
    with open(file_quote, 'r', encoding='utf-8') as f:
        quotes = json.load(f)
        for qe in quotes:
            quote = TextQuote(
                # author=author,
                author=qe['author'],
                tags=qe['tags'],
                content=qe['quote']
            ).save()


if __name__ == '__main__':

    load_json("author.json", "quotes.json")
