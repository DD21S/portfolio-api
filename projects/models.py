from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    WHITE = '#FFFFFF'
    BLACK = '#000000'
    FONT_COLORS = [
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ] 
    name = models.CharField(max_length=16, unique=True)
    font_color = models.CharField(max_length=7, choices=FONT_COLORS, default=WHITE)
    background_color = models.CharField(max_length=7)
    border_color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=40, unique=True)
    date_published = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=400)
    icon = models.CharField(max_length=12)
    link = models.URLField()
    color = models.CharField(max_length=7)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name
