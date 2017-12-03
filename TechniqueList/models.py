from datetime import datetime
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=200)


class Group(models.Model):
    name = models.CharField(max_length=200)
    position = models.ForeignKey(Position)


class Technique(models.Model):
    # url: url from Youtube
    # repetitions_done: numbers of repetitions that already done by user for this technique
    # repetitions_goal: numbers of repetitions to do by user for this technique
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)
    repetitions_done = models.IntegerField(default=0)
    repetitions_goal = models.IntegerField(default=10)
    date = models.DateTimeField(default=datetime.now)
    deleted = models.BooleanField(default=False)
    group = models.ForeignKey(Group)
