from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyUser(models.Model):
    user = models.OneToOneField(User)
    realname = models.CharField(max_length=256)
    pass_num = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.realname


class Solution(models.Model):
    num = models.IntegerField()
    url = models.CharField(max_length=256)

    def __unicode__(self):
        return self.url