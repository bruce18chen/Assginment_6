from django.db import models
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def published(self):
        return self.filter(published_date__lte=timezone.now())

class Topic(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('topic-detail', args=[str(self.slug)])

    def __str__(self):
        return self.name

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    objects = PublishedManager()  # Use the custom manager directly

    def __str__(self):
        return self.title



# other model code...


