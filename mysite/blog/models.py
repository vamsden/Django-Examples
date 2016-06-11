from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class PublishedManager(models.Manager):
    """
    Custom Model Managers
    eg: Post.published.filter(title__startswith='Who')
    """
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    # User imported as the registered User above
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
