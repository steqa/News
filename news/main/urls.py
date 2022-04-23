from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:news_id>', show_news, name='news'),
    path('country/<int:country_id>', show_country, name='country'),
]
