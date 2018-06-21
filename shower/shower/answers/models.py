from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    amount = models.DecimalField()
