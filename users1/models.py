from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images/', blank = True, null = True, verbose_name='Аватар', default='users_images/default_avatar.png')
    timezone = models.CharField(max_length=50, default='UTC')
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return self.username