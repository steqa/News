from .models import *

menu = [{'title': "Добавить новость", 'url_name': 'add_news'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        country = Country.objects.all()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
        context['menu'] = user_menu
        context['country'] = country
        if 'country_selected' not in context:
            context['country_selected'] = 0
        return context