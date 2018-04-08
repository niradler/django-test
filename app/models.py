from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


   
