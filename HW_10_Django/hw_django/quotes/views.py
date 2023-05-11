import sys
import json

# from ..hw_django.settings import BASE_DIR

from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Author, Quote
from .forms import QuoteForm, AuthorForm, TagForm
from .enemy_losses import main_enemy

sys.path.append("..")
from utils.scrapy_bs import spider_bs  # noqa


def main(request):
    path_to_enemy = "C:\PycharmProjects\HomeWork_WEB\HW_10\hw_django\quotes\json\enemy_losses.json"
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    with open(path_to_enemy, 'r', encoding='utf-8') as fd:
        enemy = json.load(fd)
    date_enemy = enemy.pop('date')

    top_tags = Quote.objects.values('tags__name', "tags__id") \
                   .annotate(quote_count=Count('tags__name')) \
                   .order_by('-quote_count')[:10]
    return render(request, "quotes/index.html", context={'quotes': page_obj, "top_tags": top_tags,
                                                         "losses_orcs": enemy, "date_enemy": date_enemy})


def author_about(request, _id):
    author = Author.objects.get(pk=_id)

    return render(request, 'quotes/author.html', context={'author': author})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_quote.html", context={'form': QuoteForm(), "message": "Form not valid"})
    return render(request, "quotes/add_quote.html", context={'form': QuoteForm()})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_author.html",
                          context={'form': AuthorForm(), "message": "Form not valid"})
    return render(request, "quotes/add_author.html", context={'form': AuthorForm()})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_tag.html", context={'form': TagForm(), "message": "Form not valid"})
    return render(request, "quotes/add_tag.html", context={'form': TagForm()})


def find_by_tag(request, _id):
    path_to_enemy = "C:\PycharmProjects\HomeWork_WEB\HW_10\hw_django\quotes\json\enemy_losses.json"
    per_page = 5
    quotes = Quote.objects.filter(tags=_id).all()
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_tags = Quote.objects.values('tags__name', "tags__id") \
                   .annotate(quote_count=Count('tags__name')) \
                   .order_by('-quote_count')[:10]

    with open(path_to_enemy, 'r', encoding='utf-8') as fd:
        enemy = json.load(fd)
    date_enemy = enemy.pop('date')
    # for tag in top_tags:
    #     tag_name = tag['tag__name']
    #     quote_count = tag['quote_count']
    #     print(f"Tag name: {tag_name}, Quote count: {quote_count}")

    return render(request, "quotes/index.html",
                  context={'quotes': page_obj, "top_tags": top_tags, "losses_orcs": enemy, "date_enemy": date_enemy})


def search_quotes(request):
    query = request.GET.get("q")
    results = []
    if query:
        quotes = Quote.objects.filter(
            Q(quote__icontains=query) | Q(author__fullname__icontains=query) | Q(tags__name__icontains=query))
        for quote in quotes:
            if quote not in results:
                results.append(quote)
        # paginator = Paginator(list(result), per_page)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        return render(request, "quotes/search.html", context={"quotes": results, "query": query})
    return redirect(to="quotes:home")


def losses_orcs(request):
    data = main_enemy()
    data = "Test data how to add you to the site"
    print("losses orcs OK")
    return render(request, "quotes/index.html", context={'losses_orcs': data})


def dont_work(request):
    return render(request, "quotes/dont_work.html", context={})


def test_func():
    for i in range(10):
        print(i)


def run_scrapy(request):
    print('Start parse')
    test_func()
    # spider_bs()
    print('Finish running')
    return redirect(to="quotes:home")
