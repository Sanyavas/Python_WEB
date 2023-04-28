from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect


from .models import Author, Quote
from .forms import QuoteForm, AuthorForm, TagForm
# import os
#
# from ..utils.main_scrapy import custom_scrapy


def main(request):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_tags = Quote.objects.values('tags__name', "tags__id") \
                   .annotate(quote_count=Count('tags__name')) \
                   .order_by('-quote_count')[:10]
    return render(request, "quotes/index.html", context={'quotes': page_obj, "top_tags": top_tags})


def author_about(request, _id):
    print(_id)
    author = Author.objects.get(pk=_id)
    print(author.fullname, type(author))

    return render(request, 'quotes/author.html', context={'author': author})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_quote.html", context={'form': QuoteForm(), "message": "Form not valid"})
    return render(request, "quotes/add_quote.html", context={'form': QuoteForm()})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_author.html",
                          context={'form': AuthorForm(), "message": "Form not valid"})
    return render(request, "quotes/add_author.html", context={'form': AuthorForm()})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:home")
        else:
            return render(request, "quotes/add_tag.html", context={'form': TagForm(), "message": "Form not valid"})
    return render(request, "quotes/add_tag.html", context={'form': TagForm()})


def find_by_tag(request, _id):
    per_page = 5
    quotes = Quote.objects.filter(tags=_id).all()
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_tags = Quote.objects.values('tags__name', "tags__id") \
                   .annotate(quote_count=Count('tags__name')) \
                   .order_by('-quote_count')[:10]
    # for tag in top_tags:
    #     tag_name = tag['tag__name']
    #     quote_count = tag['quote_count']
    #     print(f"Tag name: {tag_name}, Quote count: {quote_count}")

    return render(request, "quotes/index.html", context={'quotes': page_obj,
                                                         "top_tags": top_tags})


def run_scrapy(request):
    # custom_scrapy()
    print('Scrapy running')
    return render(request, "quotes/index.html", context={})
