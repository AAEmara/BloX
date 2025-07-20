from django.db import models
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts') 
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    publish_date = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    
    @property
    def like_count(self):
        return self.reactions.filter(is_like=True).count()

    @property
    def dislike_count(self):
        return self.reactions.filter(is_like=False).count()
    
    def __str__(self):
        return self.title

class PostReaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='reactions')
    is_like = models.BooleanField()  # if True = like, if False = dislike

    class Meta:
        unique_together = ('user', 'post')  # Ensures one reaction per user per post    