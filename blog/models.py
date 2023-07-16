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

class ContestEntry(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# other model code...


