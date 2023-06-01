import json
from pathlib import Path
import environ

import openai

from ..models import Quote, Tag, Author

THIS_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()

environ.Env.read_env(THIS_DIR / '.env')
api_key = env('API_KEY_OPENAI')
openai.api_key = api_key


def generate_qoute():
    worker = "You are a creative writer."
    prompt = """Create creative quote about poetry, poetry should be on love style.
    Quote should be on English language, and contain about 300 symbols
    Write only quote, don't add any recommendation and explanations"""
    print(f"Start request to GPT")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": worker},
            {"role": "user", "content": prompt}
        ]
    )
    with open("hw_django/quotes/json/gpt_resp.json", "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    total_tokens = response.get("usage").get("total_tokens")
    print("====================")
    print(f'Total tokens: {total_tokens}')
    print("====================")
    return response.choices[0].message.content.strip()


def add_quote_to_db(quote: str):
    author = Author.objects.filter(fullname="ChatGPT").first()
    tag = Tag.objects.get(name="poetry")
    new_quote = Quote.objects.create(quote=quote, author=author)
    new_quote.tags.add(tag)
    new_quote.save()
    print(f"New quote was added")


def gpt_creator():
    print(f"Start generation quote")
    quote = generate_qoute()
    add_quote_to_db(quote)


if __name__ == "__main__":
    print(generate_qoute())
