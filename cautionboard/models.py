from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=5)
    place = models.CharField(max_length=10) 
    caution = models.TextField()
    id=models.IntegerField(primary_key=True)
    pub_date = models.DateTimeField()
    no=models.IntegerField()
    yes= models.IntegerField()
    pet=models.BooleanField()
    tripType=models.CharField()



class Text(models.Model):
    place = models.CharField(max_length=10)
    plaInt= models.TextField()

