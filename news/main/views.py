from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    news = News.objects.order_by('-id')
    return render(request, 'main/home.html', {'news': news})

def show_news(request, news_id):
    return HttpResponse(f"News with id = {news_id}")