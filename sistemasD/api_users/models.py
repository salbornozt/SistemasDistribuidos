from django.db import models


# Create your models here.

class User(models.Model):
    idType = models.CharField(max_length=100)
    idNum = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.idNum
