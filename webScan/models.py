from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=32, blank=True, verbose_name='用户名')
    password = models.CharField(max_length=64, help_text='text')
    email = models.EmailField(max_length=60)
    pub_date = models.DateTimeField('date published')


class urlManager(models.Model):
    url = models.CharField(max_length=256, help_text='text')
    urlTime = models.DateTimeField(timezone.now)


# 储存漏洞信息表
class uV(models.Model):
    open_url = models.CharField(max_length=256, help_text='text')
    open_port = models.CharField(max_length=256, help_text='text')
    open_sql = models.CharField(max_length=256, help_text='text')
    url = models.CharField(max_length=256, help_text='text')

