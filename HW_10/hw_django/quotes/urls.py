from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='home'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<int:_id>/', views.author_about, name='author_about'),
]
