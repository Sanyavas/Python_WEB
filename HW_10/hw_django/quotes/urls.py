from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='home'),
    path('page/<int:page>/', views.main, name='root_paginate'),
    path('author/<int:_id>/', views.author_about, name='author_about'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('tag/<int:_id>/', views.find_by_tag, name='find_by_tag'),
    path('', views.run_scrapy, name='run_scrapy'),
    path('search/', views.search_quotes, name='search_quotes'),
    path('sorry/', views.dont_work, name='dont_work'),
]
