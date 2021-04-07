from django.db import models

class datos (models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
