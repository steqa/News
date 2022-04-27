from django.contrib import admin
from .models import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'time_created', 'photo', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_published', 'cat')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(News, NewsAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)