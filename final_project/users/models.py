from django.contrib.auth.models import AbstractUser
from django.db import models

CHOISE_MODEL = {
    'MobileNet_SSD': 'MobileNetSSD'
}


class User(AbstractUser):
    """Модель AbstractUser, так как добавлено поле для сохранения предопчтительной модели ИИ"""
    username = models.CharField(
        verbose_name="login",
        max_length=140,
        unique=True,
    )
    favorite_model = models.CharField(
        verbose_name='Предпочтительная модель',
        choices=CHOISE_MODEL,
        default='MobileNetSSD'
    )

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
