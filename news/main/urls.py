from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('news/<slug:news_slug>', NewsShow.as_view(), name='news'),
    path('country/<slug:country_slug>', NewsCountry.as_view(), name='country'),
    path('add-news', AddNews.as_view(), name='add_news'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
]
