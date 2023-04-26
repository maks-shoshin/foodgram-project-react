from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        'Почта',
        max_length=254,
        unique=True,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Не допускаются: пробел и символы, кроме . @ + - _',
            ),
        ]
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
    )
    password = models.CharField(
        max_length=150,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username


class Subscription(models.Model):
    """Модель для подписок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор рецепта',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'user'],
                name='unique_subscribe'
            )
        ]
