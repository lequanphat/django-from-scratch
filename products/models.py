from django.db import models

from categories.models import Category

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    def __str__(self):
        return self.name