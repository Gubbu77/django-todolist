from django.db import models

# Create your models here.
class Todolist(models.Model):
    name = models.CharField(max_length= 200)
    title = models.CharField(max_length= 1000)
    timefrom = models.CharField(max_length = 100)
    timeto = models.CharField(max_length = 100)
    done = models.BooleanField(default= False)