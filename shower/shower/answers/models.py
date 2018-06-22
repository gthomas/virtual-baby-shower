from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.TextField()

    def to_dict(self):
        pass

    def from_dict(self):
        pass

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def to_dict(self):
        pass

    def from_dict(self):
        pass

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=6)

    def to_dict(self):
        pass

    def from_dict(self):
        pass
