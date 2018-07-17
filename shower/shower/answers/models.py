from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.TextField()

    def to_dict(self):
        data = {
            'text': self.text,
        }
        return data

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    user = models.ManyToManyField(User)

    def to_dict(self):
        data = {
            'user': self.user.id,
            'question': self.question.text,
            'answer': self.answer
        }
        return data

    @classmethod
    def from_dict(cls, data):
        answer_id = data.get('pk', None)
        if answer_id:
            answer = Answer.objects.get(pk=answer_id)
        else:
            answer = Answer.objects.create()

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=6)

    def to_dict(self):
        data = {
            'user': self.user.pk,
            'note': self.note,
            'amount': self.amount
        }
        return data

    @classmethod
    def from_dict(cls, data):
        donation = Donation.objects.create()
        donation.user = data.user_id
        note = data.note
        amount = data.amount
        return donation
