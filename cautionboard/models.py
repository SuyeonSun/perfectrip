from django.db import models

class Comment(models.Model):   #사용자들이 입력한 댓글(정보). 주의사항 보여줌
    author = models.CharField(max_length=5)
    place = models.CharField(max_length=10,foreign_key=True) 
    caution = models.TextField()
    pub_date = models.DateTimeField()
    no=models.IntegerField()
    yes= models.IntegerField()
    pet=models.BooleanField()
    tripType=models.CharField(max_length=10)



class Text(models.Model):  #개발자가 입력하는 정보
    place = models.CharField(max_length=10,primary_key=True)
    placeInformation= models.TextField()


    def __str__(self) :
        return self.place