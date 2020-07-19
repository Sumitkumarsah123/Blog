from django.db import models
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title= models.CharField(max_length=20)
    writer= models.CharField(max_length=20)
    content=models.TextField()
    img=models.ImageField(upload_to='pics')
    date_posted= models.DateTimeField(default=timezone.now)

    

    
    

class Comment(models.Model):
    comment=models.TextField()
    