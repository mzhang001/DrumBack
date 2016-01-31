from django.db import models

# Create your models here.

#
# class Comment(models.Model):
#     dish_name = models.CharField(max_length=200)
#     meal = models.CharField(max_length=200) # Breakfast, Lunch, Dinner, Formal
#     date = models.DateField('the date of the meal')
#     score = models.IntegerField('the score of this meal')
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text