from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Database(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=32)
    username = models.CharField(verbose_name=_('username'), max_length=32)
    password = models.CharField(verbose_name=_('password'), max_length=32)

    def __str__(self) -> str:
        return f'<Database {self.name}>'
