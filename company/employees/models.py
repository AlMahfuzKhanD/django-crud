from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    area = models.CharField(max_length=100)
    def __str__(self):
        return self.name