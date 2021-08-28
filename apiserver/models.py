from django.db import models

# Create your models here.
class Word(models.Model):
    no = models.IntegerField(primary_key=True)
    eng = models.CharField(max_length=30)
    kor = models.TextField()
    grade = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.eng