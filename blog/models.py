#coding:utf-8
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Article(models.Model):
    title = models.CharField('title',max_length=256)
    content = models.TextField('content')
    pub_date = models.DateField('publish-time',auto_now_add = True,editable = True)
    update_time = models.DateField('update-time',auto_now=True,null=True)
    def __str__(self):
        return self.title
class Article2(models.Model):
    title = models.CharField(max_length= 100)
    category = models.CharField(max_length= 50,blank=True)
    date_time = models.DateField(auto_now_add=True)
    content = models.TextField(blank = True,null = True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']