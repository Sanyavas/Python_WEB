from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Author, Quote, Tag
from .utils import get_mongodb


def main(request):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # page_obj = paginator.page(page)
    print(page_obj)
    return render(request, "quotes/index.html", context={'quotes': page_obj})


def author_about(request, _id):
    print(_id)
    author = Author.objects.get(pk=_id)
    print(author.fullname, type(author))

    return render(request, 'quotes/author.html', context={'author': author})
