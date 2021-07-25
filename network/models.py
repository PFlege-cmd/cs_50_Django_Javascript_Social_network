from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.utils import timezone


class User(AbstractUser):
    
    def __str__(self):
        return f"{self.username}";
    
class Post(models.Model):
    content = models.TextField(max_length = 300);
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts");
    timestamp = models.DateTimeField(default= timezone.now);
    likes = models.BigIntegerField(default = 0);
    
    def __str__(self):
        return f"By: {self.author}: {self.content}";
        
    def serialize(self):
        return {
            "id" : self.id,
            "author" : self.author.username,
            "content" : self.content,
            "timestamp" : self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes" : self.likes
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post;
        fields = ['content']
    