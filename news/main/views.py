from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from .models import *
from .forms import *
from .utils import *


menu = [{'title': "Добавить новость", 'url_name': 'add_news'},
]

# Create your views here.
class NewsHome(DataMixin, ListView):
    model = News
    template_name = 'main/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(country_selected=0)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('country')
        # news = cache.get('news')
        # if not news:
        #     news = News.objects.filter(is_published=True).select_related('country')
        #     cache.set('news', news, 60)
        # return news

# def home(request):
#     news = News.objects.filter(is_published=True)
#     context = {
#         'news': news,
#         'country_selected': 0,
#     }

#     return render(request, 'main/home.html', context)


class NewsShow(DataMixin, DetailView):
    model = News
    template_name = 'main/news.html'
    slug_url_kwarg = 'news_slug'
    # context_object_name = 'news'

# def show_news(request, news_slug):
#     news = get_object_or_404(News, slug=news_slug)

#     context = {
#         'news': news,
#         'title': news.title,
#         'cat_selected': news.cat_id,
#     }

#     return render(request, 'main/news.html', context)


class NewsCountry(DataMixin, ListView):
    model = News
    template_name = 'main/home.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(country_selected=context['news'][0].country_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(country__slug=self.kwargs['country_slug'], is_published=True).select_related('country')

# def show_country(request, country_slug):
#     news = News.objects.filter(country__slug=country_slug)

#     context = {
#         'news': news,
#         'country_selected': country_slug,
#     }

#     return render(request, 'main/home.html', context)


class AddNews(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddNewsForm
    template_name = 'main/add_news.html'
    success_url = reverse_lazy('home')
    login_url = '/admin'

# def add_news(request):
#     if request.method == 'POST':
#         form = AddNewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddNewsForm()

#     context = {
#         'form': form
#     }
    
#     return render(request, 'main/add_news.html', context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')