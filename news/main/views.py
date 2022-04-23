from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    news = News.objects.order_by('-cat_id', '-id')
    country = Country.objects.all()

    context = {
        'news': news,
        'country': country,
        'country_selected': 0,
    }

    return render(request, 'main/home.html', context)


def show_news(request, news_id):
    return HttpResponse(f"News with id = {news_id}")


def show_country(request, country_id):
    news = News.objects.filter(country_id=country_id)
    country = Country.objects.all()

    context = {
        'news': news,
        'country': country,
        'country_selected': country_id,
    }

    return render(request, 'main/home.html', context)