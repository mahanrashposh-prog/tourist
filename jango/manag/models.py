from django.db import models
class manage(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

# Create your models here.
