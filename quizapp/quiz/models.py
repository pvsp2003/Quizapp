from django.db import models

# Create your models here.
class Question(models.Model):
    sub = models.CharField(max_length=100)
    qno = models.IntegerField()
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correctoption = models.CharField(max_length=255)

    class Meta:
        db_table = "question"
class Score(models.Model):
    sub = models.CharField(max_length=100)
    marks = models.IntegerField()
    class Meta:
        db_table="score"
class Log(models.Model):
    login=models.IntegerField()
    class Meta:
        db_table="log"