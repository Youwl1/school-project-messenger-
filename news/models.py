from django.conf import settings
from django.db import models

from django.contrib.auth.models import User
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title  
    def get_absolute_url(self):
        return f'/news/{self.id}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'