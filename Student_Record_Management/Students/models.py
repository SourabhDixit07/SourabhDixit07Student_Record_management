from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
