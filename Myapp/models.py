from django.db import models

# Create your models here.

class MyExpense(models.Model):

    Category = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)
    Comments = models.CharField(max_length=100)
    Created_At = models.DateTimeField( auto_now=True)
    Updated_At = models.DateTimeField( auto_now=True)