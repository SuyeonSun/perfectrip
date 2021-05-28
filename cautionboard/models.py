from django.db import models

class Text(models.Model):  #개발자가 입력하는 정보. 기준
    place = models.CharField(max_length=10,primary_key=True)
    placeInformation= models.TextField(null=False,default='')
    def __str__(self) :
        return self.place
    def summary(self):
        return self.placeInformation[:80]+'....'


class Comment(models.Model):   #사용자들이 입력한 댓글(정보). 주의사항 보여줌
    author = models.CharField(max_length=5)
    place = models.ForeignKey(Text ,on_delete=models.CASCADE,default='') 
    #ForeignKey: 1대 N관계 (Text 하나에 Comment 여러개)
    caution = models.TextField(default='')
    pub_date = models.DateTimeField(default='')
    no=models.IntegerField(default=0)
    yes= models.IntegerField(default=0)
    pet=models.BooleanField(null=False)
    tripType=models.CharField(max_length=10)
    
        