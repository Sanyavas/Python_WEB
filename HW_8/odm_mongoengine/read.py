from odm_mongoengine.models import Author, Quote
from cache import cache


@cache
def find_by_name(author):
    print(f"Find by author {author}")
    authors = Author.objects(name__iregex=author)
    for author in authors:
        quotes = Quote.objects(__raw__={"author": author.name})
        [print(f'{quote.content} {author.name}') for quote in quotes]


@cache
def find_by_tag(tag):
    list_quote = []
    quotes = Quote.objects(tags__iregex=tag)
    for quote in quotes:
        list_quote.append(quote.content)
    print(list_quote)
    [print(f'{quote.content}') for quote in quotes]
    return list_quote


@cache
def find_by_tags(tag):
    list_tags = list(tag.split(","))
    quotes = Quote.objects(tags__in=list_tags)
    [print(f'{quote.content}') for quote in quotes]


def main():
    print(f'Example:  < command:value > or < 0 > for exit')
    while True:
        try:
            us_input = input(f"\n>>> ")
            if us_input == "0":
                break
            command, value = us_input.split(":")
            if command == "name":
                find_by_name(value)
            elif command == "tag":
                find_by_tag(value)
            elif command == "tags":
                find_by_tags(value)
            else:
                print(f'Wrong command ...')

        except ValueError as err:
            print(f'ValueError {err}')
        except TypeError as err:
            print(f'TypeError {err}')
        except AttributeError as err:
            print(f'AttributeError {err}')


if __name__ == '__main__':
    main()
