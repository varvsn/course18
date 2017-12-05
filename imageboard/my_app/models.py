from django.db import models
from django.utils import timezone


class Post(models.Model):
    __tablename__ = 'posts'
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    mess_txt = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    __tablename__ = 'comments'
    post = models.ForeignKey('Post')  #related_name='id' не нужно. Будет нужно, если будет несколько FK на одну таблицу
    author = models.CharField(max_length=10)
    comment_body = models.TextField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

