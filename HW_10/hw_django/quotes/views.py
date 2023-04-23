from django.core.paginator import Paginator
from django.shortcuts import render

from .utils import get_mongodb


# Create your views here.
def main(request):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "quotes/index.html", context={'quotes': page_obj})


def author(request):
    db = get_mongodb()
    authors = db.authors.find()
    return render(request, "quotes/author.html", context={'author': authors})
