from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Event(models.Model) :
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_event")
    description = models.TextField()
    image = CloudinaryField('image', default='palceholder')
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    place = models.TextField()
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    dateEvent = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def likes_number(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='Comment')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"