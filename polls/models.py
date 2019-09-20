from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post_content = models.TextField()
    post_created_by = models.CharField(max_length=30)
    post_created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_by = models.CharField(max_length=30)
    comment_at = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()
    comment_on = models.CharField(max_length=30)
