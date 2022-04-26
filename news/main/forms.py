from django import forms
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

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'country', 'cat', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок статьи'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL-адресс статьи'}),
            'content': forms.Textarea(attrs={'rows': '5', 'class': 'form-control', 'placeholder': 'Введите текст статьи'}),
            'country': forms.Select(attrs={'class': 'form-select', 'id': 'countryvalidation',}),
            'cat': forms.Select(attrs={'class': 'form-select', 'id': 'catvalidation',}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'publishedvalidation'}),
        }