from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class AdminSite(admin.AdminSite):
    site_header = _('Auto PostgreSQL')
    site_title = _('Auto PostgreSQL')
    index_title = _('Configuration page')
