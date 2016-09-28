from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class User(models.Model):
    email = models.TextField()
    name = models.TextField()

class Task(models.Model):
    name = models.TextField()
    reel = models.TextField()
    seq = models.TextField()
    shot = models.TextField()
    start_date = models.DateField()
    end_date =models.DateField(blank=True,null=True)
    duration = models.IntegerField(blank=True,null=True,default=1)
    assignee =  models.ForeignKey(User,on_delete = models.PROTECT)

class Status(models.Model):
    task = models.ForeignKey(Task,on_delete = models.PROTECT)
    date = models.DateField(default=datetime.now())
    status_name = models.TextField(default="Not Started")
