from .models import *
from django.core.cache import cache

menu = [{'title': "Добавить новость", 'url_name': 'add_news'},
]

class DataMixin:
    paginate_by = 6
    
    def get_user_context(self, **kwargs):
        context = kwargs
        country = cache.get('country')
        if not country:
            country = Country.objects.all()
            cache.set('country', country, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
        
        context['menu'] = user_menu
        context['country'] = country
        if 'country_selected' not in context:
            context['country_selected'] = 0
        
        return context