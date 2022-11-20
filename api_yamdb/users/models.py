from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLES = [
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    ]

    role = models.CharField(
        verbose_name='Роль',
        max_length=15,
        default='user',
        choices=ROLES,
    )
    bio = models.CharField(
        verbose_name='О себе',
        max_length=500,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True,
    )

    admin_methods = ('POST', 'PUT', 'PATCH', 'DELETE',)

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_staff

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
