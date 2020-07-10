from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AutopgConfig(AppConfig):
    name = 'autopg'
    verbose_name = _('Auto PostgreSQL')
