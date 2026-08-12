from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form_control','placeholder': 'Название статьи'
                }),
            "anons": TextInput(attrs={
                'class': 'form_control','placeholder': 'Анонс статьи'
                }),
            "full_text": Textarea(attrs={
                'class': 'form_control','placeholder': 'Текст статьи'
                }),
            "date": DateTimeInput (attrs={
                'class': 'form_control','placeholder': 'Дата публикации', 'type':'datetime-local'
                }),          
        }