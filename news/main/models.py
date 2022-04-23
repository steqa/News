from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name="Локация")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk})
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Локация")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country', kwargs={'country_id': self.pk})

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'