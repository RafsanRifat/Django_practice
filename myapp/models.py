from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.name
