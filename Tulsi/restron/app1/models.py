from django.db import models

# Create your models here.
#table models---------------------/

class BookTable(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    people=models.CharField(max_length=100)
    special=models.CharField(max_length=100)
    def __str__(self):
        return self.username