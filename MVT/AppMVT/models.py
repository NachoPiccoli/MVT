from django.conf import settings
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=30)
    parentesco= models.CharField(max_length=30)
    fechadenacimiento= models.DateField()
    edad= models.IntegerField()
    jubilado= models.BooleanField()