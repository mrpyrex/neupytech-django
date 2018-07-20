from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.png', blank=True, upload_to='images/')
    
    def __str__(self):
        return self.title