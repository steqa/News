from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    news = News.objects.order_by('-cat_id', '-id')
    context = {
        'news': news,
    }
    return render(request, 'main/home.html', context)

def show_news(request, news_id):
    return HttpResponse(f"News with id = {news_id}")