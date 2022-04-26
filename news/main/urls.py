from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/<slug:news_slug>', show_news, name='news'),
    path('country/<slug:country_slug>', show_country, name='country'),
    path('add-news', add_news, name='add_news'),
]
