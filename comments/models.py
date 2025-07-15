from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,default=timezone.now)

    def is_reply(self):
        return self.parent is not None

    def __str__(self):
        return f"{self.user.username} - {self.content}"