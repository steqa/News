from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    news = News.objects.order_by('-cat_id', '-id')

    context = {
        'news': news,
        'country_selected': 0,
    }

    return render(request, 'main/home.html', context)


def show_news(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)

    context = {
        'news': news,
        'title': news.title,
        'cat_selected': news.cat_id,
    }

    return render(request, 'main/news.html', context)


def show_country(request, country_slug):
    news = News.objects.filter(country__slug=country_slug)

    context = {
        'news': news,
        'country_selected': country_slug,
    }

    return render(request, 'main/home.html', context)