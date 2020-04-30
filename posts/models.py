from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to="images", blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.title
