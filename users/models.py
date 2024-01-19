from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.TextField(validators=[
         MinLengthValidator(limit_value=8, message='Password must have at least 8 characters.'),
           MaxLengthValidator(limit_value=20, message='Password can only have a maximum of 20 characters.'),
    ])
    displayName = models.TextField(
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z ]+$',
                message='Display name can only contains letter and space.',
            ),
           MinLengthValidator(limit_value=8, message='Display name must have at least 8 characters.'),
           MaxLengthValidator(limit_value=30, message='Display name can only have a maximum of 20 characters.'),
        ]
    )
    createdAt = models.DateTimeField(default=timezone.now)
    