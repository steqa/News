from collections import UserList
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import *

class AddNewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label="Заголовок")
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Текст статьи")
    # country = forms.ModelChoiceField(queryset=Country.objects.all(), label="Локация", empty_label="Локация не выбрана")
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")
    # is_published = forms.BooleanField(label="Опубликовать", required=False, initial=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].empty_label = "Выберите локацию"
        self.fields['cat'].empty_label = "Выберите категорию"
        self.fields['photo'].empty_label = "Выберите фотографию"

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'photo', 'country', 'cat', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок статьи'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL-адресс статьи'}),
            'content': forms.Textarea(attrs={'rows': '5', 'class': 'form-control', 'placeholder': 'Введите текст статьи'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-select', 'id': 'countryvalidation',}),
            'cat': forms.Select(attrs={'class': 'form-select', 'id': 'catvalidation',}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'publishedvalidation'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 118:
            raise ValidationError('Длина превышает 118 символов')
        return title

    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2', 'placeholder': 'Повтор пароля'}))