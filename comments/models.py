from django.db import models
from django.conf import settings
from blog.models import Post

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def is_reply(self):
        return self.parent is not None

    def __str__(self):
        return f"{self.user.username} - {self.content}"