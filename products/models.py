from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.name