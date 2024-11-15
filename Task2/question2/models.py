from django.db import models

# Create your models here.

class Employee(models.Model):

    name=models.CharField(max_length=200)
    description=models.TextField(max_length=400)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField()
