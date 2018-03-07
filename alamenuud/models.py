from django.db import models
from datetime import datetime

# Create your models here.
class Alamenuu(models.Model):
    nimetus = models.CharField(max_length=50)
    tiitel = models.CharField(max_length=200)
    sisu = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nimetus
    class Meta:
        verbose_name_plural = "Alamenuud"