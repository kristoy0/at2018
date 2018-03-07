from django.db import models
from datetime import datetime
from froala_editor.fields import FroalaField

# Create your models here.
class Alamenuu(models.Model):
    nimetus = models.CharField(max_length=50)
    sisu = FroalaField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nimetus
    class Meta:
        verbose_name_plural = "Alamenüüd"

class Sundmus(models.Model):
    nimetus = models.CharField(max_length=200)
    sisu = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nimetus
    class Meta:
        verbose_name_plural = "Sündmused"

class Uudis(models.Model):
    nimetus = models.CharField(max_length=200)
    tutvustus = models.TextField(default='')
    sisu = FroalaField()
    kuupaev = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nimetus
    class Meta:
        verbose_name_plural = "Uudised"


