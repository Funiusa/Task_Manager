from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=25)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft"
        PUBLISHED = "published"

    objects = models.Manager()
    published = PublishedManager()

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    categories = models.ManyToManyField('Category', related_name='blog_posts')

    # class Meta:
    #     ordering = ("-publish", )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.published.year,
            self.published.month,
            self.published.day,
            self.slug
        ])
