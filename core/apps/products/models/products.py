from django.db import models


# Модель надо импортировать в __init__.py, чтобы джанга увидела её.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
