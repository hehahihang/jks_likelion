from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add : 생성되는 시간을 자동저장
    updated_at = models.DateTimeField(auto_now=True) # auto_now : 수정될때 시간을 자동저장
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
   
# 1:N 관계로 설정     

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
