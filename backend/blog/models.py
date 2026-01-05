from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField


class Tag(models.Model):
    """Tag's model."""

    title = models.CharField(
        max_length=100,
        verbose_name='Title',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Publish'
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return f'{self.title} - {self.is_published}'


class Post(models.Model):
    """Post's model."""

    title = models.CharField(
        max_length=250,
        verbose_name='Title',
    )
    img = models.ImageField(
        upload_to='blog/posts/',
        verbose_name='image'
    )
    content = HTMLField(
        default='Add some content here',
    )
    tag = models.ForeignKey(
        Tag, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='posts',
        verbose_name='Tag'
    )
    author = models.CharField(
        default='Надежда',
        verbose_name='Author'
    )
    date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Date',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Publish',
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return f'{self.title} - {self.author} - {self.tag} - {self.is_published}'
