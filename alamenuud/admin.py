from django.contrib import admin
from .models import Alamenuu, Sundmus, Uudis
from django import forms

admin.site.site_header = 'Administratsiooni paneel'

# Register your models here.

admin.site.register(Alamenuu)
admin.site.register(Sundmus)
admin.site.register(Uudis)