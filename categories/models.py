from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.name