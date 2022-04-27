from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    news = News.objects.filter(is_published=True)
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


def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddNewsForm()

    context = {
        'form': form
    }
    
    return render(request, 'main/add_news.html', context)